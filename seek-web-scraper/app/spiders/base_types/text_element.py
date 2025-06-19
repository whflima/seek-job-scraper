from selenium import webdriver
from selenium.webdriver.common.by import By

from app.spiders.base_types.element import BaseElement


class BaseTextElement(BaseElement):
    def __init__(self, driver: webdriver, selector: str = None, locator = By.ID):
        self.driver = driver
        super().__init__(driver=driver, locator=locator, selector=selector)
    
    def get_text_from_element(self):
        try:
            element = self.get_element()
            return element.text
        except:
            print(f"Failed to get text from element.")
            return None