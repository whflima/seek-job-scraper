from selenium import webdriver
from selenium.webdriver.common.by import By

from app.constants.enums import Selector
from app.spiders.base_types.filter import BaseFilter


class SortBy(BaseFilter):
    def __init__(self, driver: webdriver, value: str = None):
        self.value = value
        self.locator = By.XPATH
        self.selector = Selector.SORT_BY
        super().__init__(driver=driver, value=value, locator=self.locator, selector=self.selector)
    
    def sort_results(self, value: str):
        self.value = value
        return None