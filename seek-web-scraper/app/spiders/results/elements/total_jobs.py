from selenium import webdriver
from selenium.webdriver.common.by import By

from app.constants.enums import Selector
from app.spiders.base_types.text_element import BaseTextElement


class TotalJobs(BaseTextElement):
    def __init__(self, driver: webdriver):
        self.locator = By.CSS_SELECTOR
        self.selector = Selector.TOTAL_JOBS
        super().__init__(driver=driver, locator=self.locator, selector=self.selector)
    
    def get_total_jobs(self):
        return self.get_text_from_element()