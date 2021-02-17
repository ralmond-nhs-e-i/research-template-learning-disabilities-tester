## draft space for creating a more complex study definition for learning disabilities research
# semi based on ethnicity research repo
# note the original default study definition from the template is now stored under "study_definiton_example.py"

# cohort extractor
from cohortextractor import (
  StudyDefinition, 
  patients, 
  codelist_from_csv, 
  codelist, 
  filter_codes_by_category, 
  combine_codelists
  )

# import codelists
#covid_codelist = codelist(["U071", "U072"], system = "icd10")

ld_codes = codelist_from_csv(
    "codelist/rosealmond-learning-disabilities-qof-codes-primary-care-domain-reference-set-portal-4ef3a073.csv", 
    system = "snomed", 
    column = "code",
)

## STUDY POPULATION

study = StudyDefinition(  

  default_expectations = {
    "date": {"earliest": "1970-01-01", "latest": "today"}, # date range for simulation
    "rate": "uniform",
    "incidence": 0.2
  }, 
  
  population = patients.registered_with_one_practice_between(
    "2019-02-01", "2020-02-01"
  ),

  dereg_date = patients.date_deregistered_from_all_supported_practices(
    on_or_before="2020-12-01", 
    date_format = "YYYY-MM", 
    return_expectations = {"date": {"earliest":"2020-02-01"}},
    ),

  # DEMOGRAPHIC COVARIATES
  # AGE
  age = patients.age_as_of(
    "today", 
    return_expectations = {
      "rate": "universal",
      "int": {"distribution": "population_ages"},
    }
  ),

  # SEX
  sex = patients.sex(return_expectations={
    "rate": "universal", 
    "category": {"ratios":{"M": 0.49, "F":0.51}},
    }
  ),

  # DEPRIVIATION
    imd=patients.address_as_of(
        "2020-02-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        }
    ),
    # GEOGRAPHIC REGION CALLED STP
    stp=patients.registered_practice_as_of(
        "2020-02-01",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "STP1": 0.1,
                    "STP2": 0.1,
                    "STP3": 0.1,
                    "STP4": 0.1,
                    "STP5": 0.1,
                    "STP6": 0.1,
                    "STP7": 0.1,
                    "STP8": 0.1,
                    "STP9": 0.1,
                    "STP10": 0.1,
                }
            }
        }
    )







)






