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

# # Comparing prevalence of PRIMIS codelists - individual codes

import pandas as pd
import numpy as np
import os
from IPython.display import display, Markdown

# ### Load data

# +
# load data
filepath = os.path.join("..","released-outputs", "by-codelist")
file_list = os.listdir(filepath)

ddict = {}
ddict["tpp"] = {}
ddict["emis"] = {}

for item in file_list:
    string_1 = item.split('age-and-sex_')[1].replace('.csv', "") 
    codelist, system = string_1.split('__')
    df = pd.read_csv(os.path.join(filepath,item)).set_index(["ageband","sex",codelist])
    ddict[system][codelist] = df



# +
# define order in which to look at the codelist (by type)
output_order = ['carehome', 'carer', 'notcarer', 
              'bmi_stage', 'sev_obesity',
              'sev_mental', 'smhres',
              'preg', 'pregdel'
       ]

# define display headers for each group
headers = {'carehome': 'Care staff',  'carer': 'Carer / household',
  'bmi_stage': 'BMI', 
  'preg': 'Pregnancy/delivery',
  'sev_mental': 'MH'}

# load codelists for descriptions
codelists = {}
for c in output_order:
    codelists[c] = pd.read_csv(os.path.join("..","codelists","primis-covid19-vacc-uptake-"+c+".csv"))


# +
pd.set_option('display.max_rows', None)

for i in output_order:
    if i in headers:
        display(Markdown(f"## \n ## {headers[i]}"))
    df_t = ddict["tpp"][i]
    df_t = df_t.rename(columns={"rate_per_1000":"rate_per_1000 TPP"})
    df_e = ddict["emis"][i]
    df_e = df_e.rename(columns={"rate_per_1000":"rate_per_1000 EMIS"})

    df = pd.concat([df_t, df_e], axis=1)#.fillna(0)
    
        # calculate difference in rates
    #df["diff (e - t)"] = df["rate_per_1000 EMIS"] - df["rate_per_1000 TPP"]
    #df["diff (% of t)"] = round((100*df["diff (e - t)"]/df["rate_per_1000 TPP"]),1).fillna(0)
    
    df = df.reset_index()
    codelist = codelists[i]
    df = df.merge(codelist, left_on=i, right_on="code").drop("code",1)
    
    df = df.sort_values(by=["ageband", "sex", "rate_per_1000 TPP", "rate_per_1000 EMIS"], #"diff (% of t)", "diff (e - t)", "rate_per_1000 TPP"],
                            ascending = [True, True, False, False])
    df = df.set_index(["ageband","sex",i,"term"])
    
    display(df)
