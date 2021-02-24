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

df = pd.read_csv(os.path.join("..","output","input.csv"))

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

# +
# filter to valid sexes and agegroups only
df1 = df.copy().loc[(df["sex"].isin(["F","M"])) & (df["ageband"].isin(agebands))]

# for codes that are only relevant if recent (pregnancy/delivery), remove any older dates
for c in cols_recent:
    df1[(df1[c]<2020)] = np.nan

# summarise by age and gender and suppress low numbers
out = df1[cols_allyears].groupby(["ageband", "sex"]).count().transpose().replace([0,1,2,3,4],0)
out["total"] = out.sum(axis=1)

out.to_csv(os.path.join("..","safe-outputs",f"code-count-by-age-and-sex{suffix}.csv"))
out
