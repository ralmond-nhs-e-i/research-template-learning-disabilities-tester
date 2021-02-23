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

# import all codelists from codelists.py file
from codelists import *

# import all dictionaries from dictionaries.py file
from dictionaries import dict_stp

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
        "today",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5":0.2}},
        }
    ),

  # GEOGRAPHIC REGION CALLED STP
    stp = patients.registered_practice_as_of(
            "2020-01-01",
            returning="stp_code",
            return_expectations={
                "category": {"ratios": dict_stp},
            }
    ),

  # # https://codelists.opensafely.org/codelist/opensafely/severe-and-profound-learning-disability-flags/44ef542a/#full-list
    severe_and_profound_learning_disability=patients.with_these_clinical_events(
        severe_and_profound_learning_disability_codes,
        on_or_before= "today",
        returning = "binary_flag",
        return_expectations={"incidence": 0.02}, # ~1.8% of England population have a learning disability
    ),



 intel_dis_incl_downs_syndrome=patients.with_these_clinical_events(
        intellectual_disability_including_downs_syndrome_codes,
        on_or_before= "today",
        returning="binary_flag",
        return_expectations={"incidence": 0.02,},  # ~1.8% of England population have a learning disability
    )
)
