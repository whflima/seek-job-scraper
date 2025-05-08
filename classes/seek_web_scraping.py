import time
from selenium import webdriver

from utils.lib import get_all_jobs, get_job_list_applying_additional_filters, get_number_of_jobs, set_job_filters
from utils.models import Filters

work_type = ["part-time", "part time", " intern ", "internship", "sponsorship", "sponsor"]

class SeekWebScraping:
    def __init__(self, url: str = "https://www.seek.com.au/"):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        time.sleep(5)
    
    def set_filters(self, keywords: str = "Software Engineer", location: str = "All Sydney NSW", time_p: str = "Today", classification_id: str = "6281", sorted_by: str = "sortby-1"):
        set_job_filters(self.driver,  keywords, location, time_p, classification_id, sorted_by)
        time.sleep(5)
    
    def set_filters(self, filters: Filters):
        set_job_filters(self.driver, filters.keywords, filters.location, filters.time, filters.classification, filters.sort)
        time.sleep(5)
        
    def get_number_of_jobs(self):
        return get_number_of_jobs(self.driver)
    
    def get_job(self):
        number_of_jobs = self.get_number_of_jobs()
        return get_all_jobs(self.driver, number_of_jobs)
    
    def get_job_with_additional_filters(self, additional_filters):
        number_of_jobs = self.get_number_of_jobs()
        return get_job_list_applying_additional_filters(self.driver, additional_filters, number_of_jobs)
    
    def quit(self):
        self.driver.quit()