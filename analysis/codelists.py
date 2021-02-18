from cohortextractor import(
    codelist, 
    codelist_from_csv,
)

covid_codelist = codelist(["U071", "U072"], system = "icd10")


# https://codelists.opensafely.org/codelist/opensafely/severe-and-profound-learning-disability-flags/44ef542a/
severe_and_profound_learning_disability_codes = codelist_from_csv(
    "codelists/opensafely-severe-and-profound-learning-disability-flags-44ef542a.csv", 
    system = "CTV3", 
    column = "code",
)



# https://codelists.opensafely.org/codelist/opensafely/intellectual-disability-including-downs-syndrome/2020-08-27/
intellectual_disability_including_downs_syndrome_codes = codelist_from_csv(
    "codelists/opensafely-intellectual-disability-including-downs-syndrome-2020-08-27.csv",
    system="ctv3",
    column="CTV3ID",
)



