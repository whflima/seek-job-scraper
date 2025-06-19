from selenium import webdriver

from app.spiders.results.elements.summary import Summary


class Results:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.summary = Summary(driver=driver)
    
    def get_total_jobs(self):
        return self.summary.get_total_jobs()
    
    def apply_filter(self):
        return self.summary.apply_filter()