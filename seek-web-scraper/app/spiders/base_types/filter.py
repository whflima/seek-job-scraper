from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.spiders.base_types.element import BaseElement


class BaseFilter(BaseElement):
    def __init__(self, driver: webdriver, value: str = None, selector: str = None, locator = By.ID):
        self.driver = driver
        self.value = value
        super().__init__(driver=driver, locator=locator, selector=selector)
        
    def set_value(self, value: str) -> None:
        self.value = value
        
    def get_value(self) -> str:
        return self.value
    
    def apply_filter(self) -> None:
        element = self.get_element()
        element.send_keys(self.value)