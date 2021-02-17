## LIBRARIES - simple study definitions

# cohort extractor
from cohortextractor import (StudyDefinition, patients)


# dictionaries of STP codes (for dummy data)
from dictionaries import dict_stp

# set the index date 
index_date = "2020-01-01"

## STUDY POPULATION

study = StudyDefinition(
  
  default_expectations = {
    "date": {"earliest": index_date, "latest": "today"}, # date range for simulation
    "rate": "uniform",
    "incidence": 1
  }, 
  
  population = patients.registered_as_of(index_date),

 stp = patients.registered_practice_as_of(
        index_date,
        returning="stp_code",
        return_expectations={
            "category": {"ratios": dict_stp},
        }
 )
)










