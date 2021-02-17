from cohortextractor import(
    codelist, 
    codelist_from_csv,
)

covid_codelist = codelist(["U071", "U072"], system = "icd10")

ld_codes = codelist_from_csv(
    "codelists\opensafely-severe-and-profound-learning-disability-flags-44ef542a.csv", 
    system = "CTV3", 
    column = "code",
)