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

# # Comparing prevalence of PRIMIS codelists

import pandas as pd
import numpy as np
import os
from IPython.display import display, Markdown

# ### Load data

# +
# load data (note multi-level columnns)
df_e = pd.read_csv(os.path.join("..","released-outputs","code-prevalence-by-age-and-sex_emis.csv"), header=[0,1])
df_t = pd.read_csv(os.path.join("..","released-outputs","code-prevalence-by-age-and-sex_tpp.csv"), header=[0,1])

# rename some column headers
df_e = df_e.rename(columns={'Unnamed: 7_level_1': '', "ageband":'codelist', "sex":''})
df_t = df_t.rename(columns={'Unnamed: 7_level_1': '', "ageband":'codelist', "sex":''})

# set index
df_e = df_e.set_index(("codelist"))
df_t = df_t.set_index(("codelist"))


# +
# define order in which to look at the codelist (by type)
output_order = ['total_population', 
              'eth2001', 'non_eth2001', 'eth_norecord', 'eth_notgiptref','eth_notstated', 
              'longres', 
              'carehome', 'nursehome', 'domcare', 
              'carer', 'notcarer', 'hhld_imdef', 
              'shield', 'nonshield',
              'ast', 'astadm', 'astrx', 
              'bmi', 'bmi_stage', 'sev_obesity',
              'ckd15', 'ckd35', 'ckd_cov', 
              'immdx_cov', 'immrx', 
              'diab', 'dmres',
              'chd_cov', 'resp_cov', 'cld', 
              'cns_cov','spln_cov',
              'sev_mental', 'smhres', 'learndis',
              'preg', 'pregdel',               
              'cov1decl', 'cov2decl', 'covadm1', 'covadm2', 'covcontra', 'covrx',
       ]

# define display headers for each group
headers = {'total_population': 'Total population', 'eth2001': 'Ethnicity',  'longres': 'Care home resident',
  'carehome': 'Care staff',  'carer': 'Carer / household',
  'shield': 'Shielding',  'ast': 'Asthma',
  'bmi': 'BMI',  'ckd15': 'CKD',
  'immdx_cov': 'Immunodeficiency',   'diab': 'Diabetes',
  'chd_cov': ' Heart/lung conditions',
  'cns_cov':'Other conditions', 
  'preg': 'Pregnancy/delivery',              
  'sev_mental': 'MH / LD',   'cov1decl': 'Covid vax'}
# -

for i in output_order:
    if i in headers:
        display(Markdown(f"## \n ## {headers[i]}"))
        
    # find relevant row of each dataframe and rename with suffix
    t = df_t.loc[i].rename(i+" (tpp)")
    e = df_e.loc[i].rename(i+" (emis)")
    
    # concatenate into one table
    out = pd.concat([e,t], axis=1)
    
    # calculate difference in rates
    out["diff (e - t)"] = out[i+" (emis)"] - out[i+" (tpp)"]
    out["diff (% of t)"] = round((100*out["diff (e - t)"]/out[i+" (tpp)"]),1).fillna(0)
    
    display(out)
