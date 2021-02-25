import re
import requests


rsp = requests.get(
    "https://codelists.opensafely.org/api/v1/codelist/primis-covid19-vacc-uptake/?format=json"
)


records = sorted(rsp.json(), key=lambda r: r["slug"])

with open("codelists/codelists.txt", "w") as f:
    for r in records:
        f.write(r["versions"][-1]["full_slug"] + "\n")


with open("analysis/codelists.py", "w") as f:
    f.write("from cohortextractor import codelist_from_csv\n\n")

    for r in records:
        f.write("\n")
        f.write(f"# {r['name']}\n")
        f.write(f"{r['slug']} = codelist_from_csv(\n")
        f.write(f'    "codelists/primis-covid19-vacc-uptake-{r["slug"]}.csv",\n')
        f.write(f'    system="snomed",\n')
        f.write('    column="code",\n')
        f.write(")\n")


with open("analysis/study_definition.py", "w") as f:
    f.write(
        """
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
    """.strip()
        + "\n"
    )

    for r in records:
        if "drx" in r["slug"] or "eth2001_" in r["slug"]:
            # Skip these because they're subsets of other codelists
            continue

        if r["slug"] == "covrx":
            f.write(
                """
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
    ),\n"""
            )

        else:
            fn = (
                "with_these_medications"
                if "rx" in r["slug"]
                else "with_these_clinical_events"
            )

            f.write("\n")
            f.write(f"    # {r['name']}\n")
            f.write(f"    {r['slug']}=patients.{fn}(\n")
            f.write(f"        codelists.{r['slug']},\n")
            f.write(f'        returning="date",\n')
            f.write(f'        date_format="YYYY",\n')
            f.write(f"        find_last_match_in_period=True,\n")
            f.write("    ),\n")

    f.write(")")
