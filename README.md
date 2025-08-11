# OpenSAFELY PRIMIS codelist prevalence

Counts/rates of codes used for defining COVID-19 vaccine eligiblity and groupings, compared between EMIS and TPP practices (collectively), to check for any systematic differences which may impact how many patients appear eligible.

* We have used Python Notebooks to present the findings - see the [released-outputs folder](./released-outputs/).
* There is a high-level count of each codelist by age-sex groups in EMIS vs TPP and separately a deepdive which looks at each individual code within those codelists which showed the biggest differences.
* CSVs are also in [released-outputs folder](./released-outputs/).
* The data extraction is defined in the [study definition](analysis/study_definition.py); this is written in `python`, but non-programmers should be able to understand what is going on there; there is a separate study definition for the individual code analysis.
* The code lists are in the [codelists folder](./codelists/).
* Notebook templates (with dummy data) are in the [notebooks folder](./notebooks/).

# About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).
