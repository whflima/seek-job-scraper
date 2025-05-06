import time
from selenium import webdriver

from utils.lib import get_job_list_applying_additional_filters, get_number_of_jobs, set_job_filters


work_type = ["part-time", "part time", " intern ", "internship", "sponsorship", "sponsor"] 

driver = webdriver.Chrome()
driver.get("https://www.seek.com.au/")
time.sleep(5)

set_job_filters(driver, "software engineer", "All Sydney NSW", "Today", "6281", "sortby-1")
time.sleep(5)

number_of_jobs = get_number_of_jobs(driver)
job_list = get_job_list_applying_additional_filters(driver, work_type, number_of_jobs)

print(f"Number of jobs found: {number_of_jobs}")
print(f"Number of jobs filtered: {len(job_list)}")
print(f"Jobs filtered: {job_list}")

time.sleep(10)
driver.quit()


