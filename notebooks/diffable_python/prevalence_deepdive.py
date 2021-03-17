# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Prevalence of PRIMIS codelists

# +
import pandas as pd
import numpy as np
import os

suffix = f"_{os.environ.get('OPENSAFELY_BACKEND', 'tpp')}"
os.makedirs(os.path.join("..","safe-outputs","by-codelist"), exist_ok=True)
# -

# ### Load data

# +
dtypes={"sex":"category"}

df = pd.read_csv(os.path.join("..","output","input_with_codes.csv"), dtype=dtypes)

for col in df.columns:
    if col in ["patient_id", "age", "sex"]:
        continue
    if "_date" not in col: # float16 not suitable for snomed codes
        continue
    # Most columns only contain years or NaN so we can store them as
    # float16s, which saves a lot of memory
    df[col] = df[col].astype("float16")

# -

# ### Create ageband

# +
agebands = ['16-39', '40-69', '70+']
conditions = [
    (df['age'] >= 16) & (df['age'] < 40),
    (df['age'] >= 40) & (df['age'] < 70),
    (df['age'] >= 70) & (df['age'] < 120)]
choices = agebands
df['ageband'] = np.select(conditions, choices, default=np.nan)

# filter to largest sex groups
df['sex'] = np.where(df['sex'].isin(['I','U']), np.nan, df["sex"])
# -

# ### Summarise data

# list columns of interest 
cols_allyears = [c for c in df.columns if ((c not in ["age","patient_id"]) & ("_date" not in c))]
cols_recent = ["preg", "pregdel"]

# filter to valid sexes and agegroups only
df1 = df.copy().loc[(df["sex"].isin(["F","M"])) & (df["ageband"].isin(agebands))]

# ### Calculate population denominators

# +

out2 = df1.groupby(["ageband", "sex"])[["patient_id"]].nunique().rename(columns={"patient_id":"total_population"}).transpose()

# calculate total population across all ages and sexes
out2["total"] = out2.sum(axis=1)

out2
# -

# ### Codelist counts

# +
# for codes that are only relevant if recent (pregnancy/delivery), remove any older dates
for c in cols_recent:
    df1.loc[(df1[f"{c}_date"]<2020), c] = np.nan

# exclude date columns
out = df1.copy()[cols_allyears]
    
# summarise most common codes for each codelist, by age and gender
for c in out.columns.drop(["sex", "ageband"]):
    # count number of occurrences for each code by ageband and sex:
    out = df1.groupby(["ageband", "sex",c])["patient_id"].nunique().reset_index()
    out = out.rename(columns={"patient_id":"patient_count"})
    
    out[c] = out[c].astype(int)
    
    # rank codes by number of occurrences
    out["rank"] = out.groupby(["ageband", "sex"])[["patient_count"]].rank(method="min", ascending=False)
    
    # keep top 10 codes and those with more than 10 occurrences only
    out = out[(out["rank"]<=10) & (out["patient_count"]>10)].drop("rank", axis=1)
    
    
    # join population denominators
    out = out.set_index(["ageband", "sex"])
    out = out.join(out2.transpose())    

    # calculate rates
    out["rate_per_1000"] = (1000*(out["patient_count"]/out["total_population"]))
    
    # round based on values
    dp = 1
    if out["rate_per_1000"].max() <1:
        dp = 2
    out["rate_per_1000"] = out["rate_per_1000"].round(dp)
    
    out = out.drop(["patient_count","total_population"], 1)

    display(out)

    # export to csv    
    out.to_csv(os.path.join("..","safe-outputs","by-codelist",f"code-prevalence-by-age-and-sex_{c}_{suffix}.csv"))


