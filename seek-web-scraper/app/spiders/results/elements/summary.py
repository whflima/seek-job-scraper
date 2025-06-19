from selenium import webdriver

from app.spiders.results.elements.sort_by import SortBy
from app.spiders.results.elements.total_jobs import TotalJobs


class Summary:
    def __init__(self, driver: webdriver):
        self.total_jobs = TotalJobs(driver=driver) 
        self.sort_by = SortBy(driver=driver) 
    
    def get_total_jobs(self):
        return int(self.total_jobs.get_text_from_element())
    
    def sort_results(self, value: str):
        return self.sort_by.sort_results(value)