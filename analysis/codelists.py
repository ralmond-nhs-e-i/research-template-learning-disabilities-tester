from cohortextractor import(
    codelist, 
    codelist_from_csv,
)

covid_codelist = codelist(["U071", "U072"], system = "icd10")

ld_codes = codelist_from_csv(
    "codelist/rosealmond-learning-disabilities-qof-codes-primary-care-domain-reference-set-portal-4ef3a073.csv", 
    system = "snomed", 
    column = "code",
)