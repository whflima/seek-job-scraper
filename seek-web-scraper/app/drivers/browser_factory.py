from selenium import webdriver


def get_chrome_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    return webdriver.Chrome(options=options)