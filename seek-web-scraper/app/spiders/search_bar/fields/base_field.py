from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver: webdriver, value: str = None, selector: str = None, locator = By.ID):
        self.driver = driver
        self.value = value
        self.selector = selector
        self.locator = locator
        
    def set_value(self, value: str) -> None:
        self.value = value
        
    def get_value(self) -> str:
        return self.value
    
    def get_element(self, retries=3):
        for attempt in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((self.locator, self.selector)))
                return element
            except:
                if attempt == retries - 1:
                    raise Exception(f"Failed to get element: {self.selector}.")
    
    def apply_filter(self) -> None:
        element = self.get_element()
        element.send_keys(self.value)