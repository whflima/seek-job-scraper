from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver: webdriver, selector: str = None, locator = By.ID):
        self.driver = driver
        self.selector = selector
        self.locator = locator
    
    def get_element(self, retries=3):
        for attempt in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((self.locator, self.selector)))
                return element
            except:
                if attempt == retries - 1:
                    raise Exception(f"Failed to get element: {self.selector}.")
    
    def click_element(self):
        try:
            element = self.get_element()
            element.click()
        except:
            print("Click intercepted, using JavaScript to click the element.")
            self.driver.execute_script("arguments[0].click();", element)