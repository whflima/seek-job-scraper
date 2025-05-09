from tempfile import mkdtemp
import time
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.lib import get_all_jobs, get_job_list_applying_additional_filters, get_number_of_jobs, set_job_filters
from utils.models import Filters

work_type = ["part-time", "part time", " intern ", "internship", "sponsorship", "sponsor"]

class SeekWebScraping:
    def __init__(self, url: str = "https://www.seek.com.au/"):
        self.driver = self._get_chrome_driver()
        self.driver.get(url)
        time.sleep(5)
    
    def _get_chrome_driver(self):
        if platform.system() == 'Windows':
            return webdriver.Chrome()
        
        chrome_service = self._get_chrome_service()
        chrome_options = self._get_chrome_options()
        return webdriver.Chrome(options=chrome_options, service=chrome_service)
    
    def _get_chrome_service(self):
        service = webdriver.ChromeService("/opt/chromedriver")
        return service
    
    def _get_chrome_options(self):
        chrome_options = Options()
        chrome_options.binary_location = '/opt/chrome/chrome'
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280x1696")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-dev-tools")
        chrome_options.add_argument("--no-zygote")
        chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
        chrome_options.add_argument(f"--data-path={mkdtemp()}")
        chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("user-agent=Mozilla/5.0 ... Chrome/113.0.0.0 Safari/537.36")
        return chrome_options

    def set_filters(self, keywords: str = "Software Engineer", location: str = "All Sydney NSW", time_p: str = "Today", classification_id: str = "6281", sorted_by: str = "sortby-1"):
        set_job_filters(self.driver,  keywords, location, time_p, classification_id, sorted_by)
        time.sleep(5)
    
    def set_filters(self, filters: Filters):
        set_job_filters(self.driver, filters.keywords, filters.location, filters.time, filters.classification, filters.sort)
        time.sleep(5)
        
    def get_number_of_jobs(self):
        return get_number_of_jobs(self.driver)
    
    def get_job(self):
        number_of_jobs = self.get_number_of_jobs()
        return get_all_jobs(self.driver, number_of_jobs)
    
    def get_job_with_additional_filters(self, additional_filters):
        number_of_jobs = self.get_number_of_jobs()
        return get_job_list_applying_additional_filters(self.driver, additional_filters, number_of_jobs)
    
    def quit(self):
        self.driver.quit()