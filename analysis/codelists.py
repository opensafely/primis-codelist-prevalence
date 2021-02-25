from cohortextractor import codelist_from_csv


# Asthma Diagnosis code
ast = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-ast.csv",
    system="snomed",
    column="code",
)

# Asthma Admission codes
astadm = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-astadm.csv",
    system="snomed",
    column="code",
)

# Asthma systemic steroid prescription codes
astrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-astrx.csv",
    system="snomed",
    column="code",
)

# Oxford AstraZeneca vaccination medication code
azdrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-azdrx.csv",
    system="snomed",
    column="code",
)

# BMI
bmi = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-bmi.csv",
    system="snomed",
    column="code",
)

# All BMI coded terms
bmi_stage = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-bmi_stage.csv",
    system="snomed",
    column="code",
)

# Employed by Care Home codes
carehome = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-carehome.csv",
    system="snomed",
    column="code",
)

# Carer codes
carer = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-carer.csv",
    system="snomed",
    column="code",
)

# Chronic heart disease codes
chd_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-chd_cov.csv",
    system="snomed",
    column="code",
)

# Chronic kidney disease codes - all stages
ckd15 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-ckd15.csv",
    system="snomed",
    column="code",
)

# Chronic kidney disease codes-stages 3 - 5
ckd35 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-ckd35.csv",
    system="snomed",
    column="code",
)

# Chronic kidney disease diagnostic codes
ckd_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-ckd_cov.csv",
    system="snomed",
    column="code",
)

# Chronic Liver disease codes
cld = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-cld.csv",
    system="snomed",
    column="code",
)

# Chronic Neurological Disease including Significant Learning Disorder
cns_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-cns_cov.csv",
    system="snomed",
    column="code",
)

# First COVID vaccination declined
cov1decl = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-cov1decl.csv",
    system="snomed",
    column="code",
)

# Second COVID vaccination declined
cov2decl = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-cov2decl.csv",
    system="snomed",
    column="code",
)

# First COVID vaccination administration codes
covadm1 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-covadm1.csv",
    system="snomed",
    column="code",
)

# Second COVID vaccination administration codes
covadm2 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-covadm2.csv",
    system="snomed",
    column="code",
)

# COVID vaccination contraindication codes
covcontra = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-covcontra.csv",
    system="snomed",
    column="code",
)

# COVID vaccination medication code (any)
covrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-covrx.csv",
    system="snomed",
    column="code",
)

# Diabetes diagnosis codes
diab = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-diab.csv",
    system="snomed",
    column="code",
)

# Diabetes resolved codes
dmres = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-dmres.csv",
    system="snomed",
    column="code",
)

# Employed by domiciliary care provider codes
domcare = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-domcare.csv",
    system="snomed",
    column="code",
)

# Ethnicity codes
eth2001 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001.csv",
    system="snomed",
    column="code",
)

# Asian or Asian British - Bangladeshi Ethnicity
eth2001_asnbang = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_asnbang.csv",
    system="snomed",
    column="code",
)

# Asian or Asian British - Indian Ethnicity
eth2001_asnindian = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_asnindian.csv",
    system="snomed",
    column="code",
)

# Asian or Asian British - Any other Asian background Ethnicity
eth2001_asnother = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_asnother.csv",
    system="snomed",
    column="code",
)

# Asian or Asian British - Pakistani Ethnicity
eth2001_asnpak = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_asnpak.csv",
    system="snomed",
    column="code",
)

# Black or Black British - African Ethnicity
eth2001_blkafric = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_blkafric.csv",
    system="snomed",
    column="code",
)

# Black or Black British - Caribbean Ethnicity
eth2001_blkcarib = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_blkcarib.csv",
    system="snomed",
    column="code",
)

# Black or Black British - Any other Black background Ethnicity
eth2001_blkoth = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_blkoth.csv",
    system="snomed",
    column="code",
)

# Other ethnic groups - Chinese Ethnicity
eth2001_chinese = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_chinese.csv",
    system="snomed",
    column="code",
)

# Mixed - Any other mixed background Ethnicity
eth2001_mxdother = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_mxdother.csv",
    system="snomed",
    column="code",
)

# Mixed - White and Asian Ethnicity
eth2001_mxdwhiasn = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_mxdwhiasn.csv",
    system="snomed",
    column="code",
)

# Mixed - White and Black African Ethnicity
eth2001_mxdwhiblkafr = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_mxdwhiblkafr.csv",
    system="snomed",
    column="code",
)

# Mixed - White and Black Caribbean Ethnicity
eth2001_mxdwhiblkcar = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_mxdwhiblkcar.csv",
    system="snomed",
    column="code",
)

# Other ethnic groups - Any other ethnic group Ethnicity
eth2001_other = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_other.csv",
    system="snomed",
    column="code",
)

# White British Ethnicity
eth2001_whibrit = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_whibrit.csv",
    system="snomed",
    column="code",
)

# White Irish Ethnicity
eth2001_whiirish = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_whiirish.csv",
    system="snomed",
    column="code",
)

# White - Any other White background Ethnicity
eth2001_whiother = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001_whiother.csv",
    system="snomed",
    column="code",
)

# Ethnicity no record
eth_norecord = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_norecord.csv",
    system="snomed",
    column="code",
)

# Ethnicity not given - patient refused
eth_notgiptref = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_notgiptref.csv",
    system="snomed",
    column="code",
)

# Ethnicity not stated
eth_notstated = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_notstated.csv",
    system="snomed",
    column="code",
)

# to represent household contact of shielding individual
hhld_imdef = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-hhld_imdef.csv",
    system="snomed",
    column="code",
)

# Immunosuppression diagnosis codes
immdx_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-immdx_cov.csv",
    system="snomed",
    column="code",
)

# Immunosuppression medication codes
immrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-immrx.csv",
    system="snomed",
    column="code",
)

# Janssen vaccination medication code
jndrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-jndrx.csv",
    system="snomed",
    column="code",
)

# Wider Learning Disability
learndis = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-learndis.csv",
    system="snomed",
    column="code",
)

# Patients in long-stay nursing and residential care
longres = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-longres.csv",
    system="snomed",
    column="code",
)

# Moderna vaccination medication code
modrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-modrx.csv",
    system="snomed",
    column="code",
)

# Any other ethnicity code
non_eth2001 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-non_eth2001.csv",
    system="snomed",
    column="code",
)

# Lower Risk from COVID-19 codes
nonshield = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-nonshield.csv",
    system="snomed",
    column="code",
)

# No longer a carer codes
notcarer = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-notcarer.csv",
    system="snomed",
    column="code",
)

# Employed by nursing home codes
nursehome = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-nursehome.csv",
    system="snomed",
    column="code",
)

# Pfizer BioNTech vaccination medication code
pfdrx = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-pfdrx.csv",
    system="snomed",
    column="code",
)

# Pregnancy codes recorded in the 8.5 months before the audit run date
preg = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-preg.csv",
    system="snomed",
    column="code",
)

# Pregnancy or Delivery codes recorded in the 8.5 months before audit run date
pregdel = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-pregdel.csv",
    system="snomed",
    column="code",
)

# Chronic Respiratory Disease
resp_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-resp_cov.csv",
    system="snomed",
    column="code",
)

# Severe Mental Illness codes
sev_mental = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-sev_mental.csv",
    system="snomed",
    column="code",
)

# Severe Obesity code recorded
sev_obesity = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-sev_obesity.csv",
    system="snomed",
    column="code",
)

# High Risk from COVID-19 code
shield = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-shield.csv",
    system="snomed",
    column="code",
)

# Remission codes relating to Severe Mental Illness
smhres = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-smhres.csv",
    system="snomed",
    column="code",
)

# Asplenia or Dysfunction of the Spleen codes
spln_cov = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-spln_cov.csv",
    system="snomed",
    column="code",
)
