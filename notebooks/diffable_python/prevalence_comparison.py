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
os.makedirs(os.path.join("..","safe-outputs"), exist_ok=True)
# -

# ### Load data

# +
# import first row to get col names
df_head = pd.read_csv(os.path.join("..","output","input.csv"), nrows=1)

# filter out columns not needed
cols_all = df_head.columns
cols_to_use = [c for c in cols_all if c not in ["hashed_organisation", "patient_id"]]

# import full dataset without columns not needed
df = pd.read_csv(os.path.join("..","output","input.csv"), usecols=cols_to_use)

for col in df.columns:
    if col in ["age", "sex"]:
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
df['sex'] = df['sex'].replace(['I','U'], np.nan)

# -

# ### Summarise data

# list columns of interest 
cols_allyears = [c for c in df.columns if c not in ["age","patient_id"]]
cols_recent = ["preg", "pregdel"]

# filter to valid sexes and agegroups only
df1 = df.copy().loc[(df["sex"].isin(["F","M"])) & (df["ageband"].isin(agebands))]

# ### Calculate population denominators

# +

out2 = df1.groupby(["ageband", "sex"])[["registered"]].count().rename(columns={"registered":"total_population"}).transpose()

# calculate total population across all ages and sexes
out2["total"] = out2.sum(axis=1)

out2
# -

# ### Codelist counts

# +
# for codes that are only relevant if recent (pregnancy/delivery), remove any older dates
for c in cols_recent:
    df1.loc[(df1[c]<2020), c] = np.nan

# summarise by age and gender
out = df1[cols_allyears].groupby(["ageband", "sex"]).count().transpose()

# suppress low numbers
out = out.replace([0,1,2,3,4,5],0)

# calculate total count for each codelist across all ages and sexes
out["total"] = out.sum(axis=1)

# add population denominators
out = pd.concat([out,out2])

display(out.tail())

# export to csv

out_exp = out.copy()
out_exp = 5*((out_exp/5).round(0)).astype(int)
out_exp = out_exp.replace([0,5], "<8")

# additional check for small numbers of suppressed small numbers
for i in out_exp.index:
    check = out_exp.transpose().groupby(i).agg({i:"count"})
    if "<8" in check.index:
        # if only 1-2 suppressed value(s) appears in row, apply additional suppression
        if (check.loc["<8"][0]<=2) & (10 in check.index):
            out_exp = out_exp.replace(["<8", 10], "<13")
        elif (check.loc["<8"][0]<=2) & (10 not in check.index):
            out_exp = out_exp.replace(["<8", 15], "<18")

out_exp.to_csv(os.path.join("..","safe-outputs",f"code-counts-by-age-and-sex{suffix}.csv"))

# -

# ### Codelist prevalence rates

# +
# calculate rates
for i in out.index.drop("total_population"):
    out.loc[i] = (1000*out.loc[i]/out.loc["total_population"]).round(1)
    
# export to csv    
out.to_csv(os.path.join("..","safe-outputs",f"code-prevalence-by-age-and-sex{suffix}.csv"))

out
