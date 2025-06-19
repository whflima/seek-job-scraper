from selenium import webdriver
from app.constants.enums import Selector
from app.spiders.search_bar.fields.base_field import BaseFilter


class Classification(BaseFilter):
    def __init__(self, driver: webdriver, value: str = None):
        self.locator = ""
        self.selector = Selector.CLASSIFICATION
        super().__init__(driver=driver, value=value, locator=self.locator, selector=self.selector)
    
    def get_element(self):
        return None    
    
    def apply_filter(self):
        return None