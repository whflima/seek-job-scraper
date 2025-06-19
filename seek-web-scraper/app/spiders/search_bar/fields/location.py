from selenium import webdriver
from selenium.webdriver.common.by import By
from app.constants.enums import Selector
from app.spiders.base_types.filter import BaseFilter


class Location(BaseFilter):
    def __init__(self, driver: webdriver, value: str = None):
        self.locator = By.ID
        self.selector = Selector.LOCATION
        super().__init__(driver=driver, value=value, locator=self.locator, selector=self.selector)