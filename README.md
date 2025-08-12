# OpenSAFELY PRIMIS codelist prevalence

Counts/rates of codes used for defining COVID-19 vaccine eligiblity and groupings, compared between EMIS and TPP practices (collectively), to check for any systematic differences which may impact how many patients appear eligible.

* We have used Python Notebooks to present the findings - see the [released-outputs folder](./released-outputs/).
* There are two levels to the results:
    1.  a high-level count of each codelist by age-sex groups in EMIS vs TPP, and
    2.  a deepdive which examines the most common individual codes within those codelists which showed the biggest differences.
* The code lists assessed are in the [codelists folder](./codelists/).
* The initial data extraction for (1) is defined in the [study definition](analysis/study_definition.py); and for (2) in [study definition](analysis/study_definition_with_codes.py).
* Notebook templates (with dummy data) which were used to process the anonymised patient-level data extracts into counts and rates are in the [notebooks folder](./notebooks/).
* Results as CSVs are in [released-outputs folder](./released-outputs/).
  
# About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).
