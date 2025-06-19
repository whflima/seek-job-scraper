from enum import Enum

class Selector(Enum):
    KEYWORDS = "keywords-input"
    CLASSIFICATION = ""
    LOCATION = "SearchBar__Where"
    TOTAL_JOBS = "totalJobsCount"
    SORT_BY = "//span[contains(text(), 'Sorted by')]"