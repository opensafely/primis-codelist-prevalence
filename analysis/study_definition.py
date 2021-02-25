from datetime import date

from cohortextractor import StudyDefinition, patients
import codelists


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.1,
    },

    population=patients.satisfying("age >= 16 AND age <= 120"),

    age=patients.age_as_of(
        "2021-03-31",  # PRIMIS REF_DAT
        return_expectations={
            "int": {"distribution": "population_ages"},
            "rate": "universal",
        },
    ),

    sex=patients.sex(
        return_expectations={
            "category": {"ratios": {"F": 0.49, "M": 0.49, "U": 0.01, "I": 0.01}},
            "rate": "universal",
        },
    ),

    # Asthma Diagnosis code
    ast=patients.with_these_clinical_events(
        codelists.ast,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Asthma Admission codes
    astadm=patients.with_these_clinical_events(
        codelists.astadm,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Asthma systemic steroid prescription codes
    astrx=patients.with_these_medications(
        codelists.astrx,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # BMI
    bmi=patients.with_these_clinical_events(
        codelists.bmi,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # All BMI coded terms
    bmi_stage=patients.with_these_clinical_events(
        codelists.bmi_stage,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Employed by Care Home codes
    carehome=patients.with_these_clinical_events(
        codelists.carehome,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Carer codes
    carer=patients.with_these_clinical_events(
        codelists.carer,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic heart disease codes
    chd_cov=patients.with_these_clinical_events(
        codelists.chd_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic kidney disease codes - all stages
    ckd15=patients.with_these_clinical_events(
        codelists.ckd15,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic kidney disease codes-stages 3 - 5
    ckd35=patients.with_these_clinical_events(
        codelists.ckd35,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic kidney disease diagnostic codes
    ckd_cov=patients.with_these_clinical_events(
        codelists.ckd_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic Liver disease codes
    cld=patients.with_these_clinical_events(
        codelists.cld,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic Neurological Disease including Significant Learning Disorder
    cns_cov=patients.with_these_clinical_events(
        codelists.cns_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # First COVID vaccination declined
    cov1decl=patients.with_these_clinical_events(
        codelists.cov1decl,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Second COVID vaccination declined
    cov2decl=patients.with_these_clinical_events(
        codelists.cov2decl,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # First COVID vaccination administration codes
    covadm1=patients.with_these_clinical_events(
        codelists.covadm1,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Second COVID vaccination administration codes
    covadm2=patients.with_these_clinical_events(
        codelists.covadm2,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # COVID vaccination contraindication codes
    covcontra=patients.with_these_clinical_events(
        codelists.covcontra,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    covrx=patients.with_vaccination_record(
        tpp={
            "product_name_matches": ["COVID-19 mRNA Vac BNT162b2 30mcg/0.3ml conc for susp for inj multidose vials (Pfizer-BioNTech)", "COVID-19 Vac AstraZeneca (ChAdOx1 S recomb) 5x10000000000 viral particles/0.5ml dose sol for inj MDV", "TODO", "TODO"],
        },
        emis={
            "product_codes": codelists.covrx,
        },
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Diabetes diagnosis codes
    diab=patients.with_these_clinical_events(
        codelists.diab,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Diabetes resolved codes
    dmres=patients.with_these_clinical_events(
        codelists.dmres,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Employed by domiciliary care provider codes
    domcare=patients.with_these_clinical_events(
        codelists.domcare,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Ethnicity codes
    eth2001=patients.with_these_clinical_events(
        codelists.eth2001,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Ethnicity no record
    eth_norecord=patients.with_these_clinical_events(
        codelists.eth_norecord,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Ethnicity not given - patient refused
    eth_notgiptref=patients.with_these_clinical_events(
        codelists.eth_notgiptref,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Ethnicity not stated
    eth_notstated=patients.with_these_clinical_events(
        codelists.eth_notstated,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # to represent household contact of shielding individual
    hhld_imdef=patients.with_these_clinical_events(
        codelists.hhld_imdef,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Immunosuppression diagnosis codes
    immdx_cov=patients.with_these_clinical_events(
        codelists.immdx_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Immunosuppression medication codes
    immrx=patients.with_these_medications(
        codelists.immrx,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Wider Learning Disability
    learndis=patients.with_these_clinical_events(
        codelists.learndis,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Patients in long-stay nursing and residential care
    longres=patients.with_these_clinical_events(
        codelists.longres,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Any other ethnicity code
    non_eth2001=patients.with_these_clinical_events(
        codelists.non_eth2001,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Lower Risk from COVID-19 codes
    nonshield=patients.with_these_clinical_events(
        codelists.nonshield,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # No longer a carer codes
    notcarer=patients.with_these_clinical_events(
        codelists.notcarer,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Employed by nursing home codes
    nursehome=patients.with_these_clinical_events(
        codelists.nursehome,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Pregnancy codes recorded in the 8.5 months before the audit run date
    preg=patients.with_these_clinical_events(
        codelists.preg,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Pregnancy or Delivery codes recorded in the 8.5 months before audit run date
    pregdel=patients.with_these_clinical_events(
        codelists.pregdel,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Chronic Respiratory Disease
    resp_cov=patients.with_these_clinical_events(
        codelists.resp_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Severe Mental Illness codes
    sev_mental=patients.with_these_clinical_events(
        codelists.sev_mental,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Severe Obesity code recorded
    sev_obesity=patients.with_these_clinical_events(
        codelists.sev_obesity,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # High Risk from COVID-19 code
    shield=patients.with_these_clinical_events(
        codelists.shield,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Remission codes relating to Severe Mental Illness
    smhres=patients.with_these_clinical_events(
        codelists.smhres,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),

    # Asplenia or Dysfunction of the Spleen codes
    spln_cov=patients.with_these_clinical_events(
        codelists.spln_cov,
        returning="date",
        date_format="YYYY",
        find_last_match_in_period=True,
    ),
)