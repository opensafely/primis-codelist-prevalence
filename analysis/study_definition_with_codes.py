from datetime import date

from cohortextractor import StudyDefinition, patients
import codelists


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.1,
        #"category": {"ratios": {"12345": 0.5, "67890": 0.5, }},
    },

    population=patients.satisfying("registered AND age >= 16 AND age <= 120"),

    registered=patients.registered_as_of(
        "2020-03-31",  # PRIMIS REF_DAT
        return_expectations={
            "incidence": 0.95,
        },
    ),

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

    # All BMI coded terms
    bmi_stage=patients.with_these_clinical_events(
        codelists.bmi_stage,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"35425004": 0.5, "819948005": 0.5, }},
                },
    ),

    # Employed by Care Home codes
    carehome=patients.with_these_clinical_events(
        codelists.carehome,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"1092561000000107": 0.95, "158944006": 0.05, }},
                },
    ),

    # Carer codes
    carer=patients.with_these_clinical_events(
        codelists.carer,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"407542009": 0.5, "276048003": 0.5, }},
                },
    ),

    # No longer a carer codes
    notcarer=patients.with_these_clinical_events(
        codelists.notcarer,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"199361000000101": 0.5, "506401000000109": 0.5, }},
                },
    ),

    # Pregnancy codes recorded in the 8.5 months before the audit run date
    preg=patients.with_these_clinical_events(
        codelists.preg,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"77386006": 0.5, "80487005": 0.5, }},
                },
    ),

    # Pregnancy or Delivery codes recorded in the 8.5 months before audit run date
    pregdel=patients.with_these_clinical_events(
        codelists.pregdel,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"3950001": 0.5, "16356006": 0.5, }},
                },
    ),

    # Severe Mental Illness codes
    sev_mental=patients.with_these_clinical_events(
        codelists.sev_mental,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"13746004": 0.5, "49468007": 0.5, }},
                },
    ),

    # Severe Obesity code recorded
    sev_obesity=patients.with_these_clinical_events(
        codelists.sev_obesity,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.1,
                "category": {"ratios": {"819948005": 0.34, "408512008": 0.33, "914741000000103": 0.33}},
                },
    ),


    # Remission codes relating to Severe Mental Illness
    smhres=patients.with_these_clinical_events(
        codelists.smhres,
        returning="code",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
                "incidence": 0.05,
                "category": {"ratios": {"41836007": 0.5, "698951002": 0.5, }},
                },
    ),


)