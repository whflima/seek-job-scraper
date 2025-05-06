import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element(driver, locator, selector, retries=3):
    for attempt in range(retries):
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((locator, selector)))
            return element
        except:
            if attempt == retries - 1:
                raise Exception(f"Failed to get element: {selector}.")

def get_attribute_from_element(element, attribure):
    try:
        return element.get_attribute(attribure)
    except:
        print(f"Failed to get attribute {attribure} from element.")
        return None

def get_text_from_element(element):
    try:
        return element.text
    except:
        print(f"Failed to get text from element.")
        return None

def click_element(driver, element):
    try:
        element.click()
    except:
        print("Click intercepted, using JavaScript to click the element.")
        driver.execute_script("arguments[0].click();", element)

def click_element_by_id(driver, element_id):
    element = get_element(driver, By.ID, element_id)
    click_element(driver, element)

def get_job_link(driver, job_id):
    selector = f'job-title-{job_id}'
    return get_element(driver, By.ID, selector)

def get_job_ad_details_element(driver, job_id):
    job_link_element = get_job_link(driver, job_id)
    click_element(driver, job_link_element)

    selector = '[data-automation="jobAdDetails"]'
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_classification_toggle(driver, timeout=10):
    selector = '[data-automation="toggleClassificationPanel"]'
    try:
        return get_element(driver, By.CSS_SELECTOR, selector)
    except:
        print(f"Failed to get job classification toggle element.")
        return None

def get_job_classification_element(driver):
    classification_toggle = get_classification_toggle(driver)
    if classification_toggle != None:
        return classification_toggle
    
    selector = '[data-automation="classificationDropDownList"]'
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_job_listing_time_element(driver):
    selector = '[data-automation="toggleDateListedPanel"]'
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_job_listing_time_radio_element(driver, listing_time):
    selector = f'a[aria-label="{listing_time}"]'
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_job_classification_checkbox_element(driver, classification_id):
    selector = f'a[data-automation="{classification_id}"]'
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_next_job_card(driver, card_number, retries=1):
    selector = f'jobcard-{card_number}'
    try:
        return get_element(driver, By.ID, selector, retries)
    except Exception as e:
        print(e)
        return None

def get_next_job_page(driver, page):
    selector = f"a[data-automation='page-{page}']"
    try:
        return get_element(driver, By.CSS_SELECTOR, selector)
    except Exception as e:
        print(e)
        return None

def get_sorted_by_option_element(driver, tag):
    selector = f"a[data-automation='{tag}']"
    return get_element(driver, By.CSS_SELECTOR, selector)

def get_sorted_by_element(driver):
    selector = "//span[contains(text(), 'Sorted by')]"
    return get_element(driver, By.XPATH, selector)

def get_number_of_jobs(driver):
    selector = '[data-automation="totalJobsCount"]'
    element = get_element(driver, By.CSS_SELECTOR, selector)
    return int(get_text_from_element(element))

def set_listing_time_radio(driver, listing_time):
    listing_time_element = get_job_listing_time_element(driver)
    click_element(driver, listing_time_element)
    time.sleep(1)

    listing_time_radio_element = get_job_listing_time_radio_element(driver, listing_time)
    click_element(driver, listing_time_radio_element)
    
def set_classification_checkbox(driver, classification_id):
    job_classification_element = get_job_classification_element(driver)
    click_element(driver, job_classification_element)
    time.sleep(1)

    job_classification_checkbox_element = get_job_classification_checkbox_element(driver, classification_id)
    click_element(driver, job_classification_checkbox_element)

def set_sorted_by(driver, tag):
    sorted_by_element = get_sorted_by_element(driver)
    click_element(driver, sorted_by_element)

    sort_by_date = get_sorted_by_option_element(driver, tag)
    click_element(driver, sort_by_date)

def get_job_info(driver, card_id, card_title, job_description):
    job_link = get_job_link(driver, card_id) 
    link_href = get_attribute_from_element(job_link, 'href')

    return {
        "id": card_id,
        "title": card_title,
        "description": job_description,
        "href" : link_href
    }

def is_job_matches(additional_filters, job):
    found = [item for item in additional_filters if item in job]
    return len(found) != 0

def is_job_matches_with_additional_filters(additional_filters, card_title, card_body):
    return is_job_matches(additional_filters, card_title) or is_job_matches(additional_filters, card_body)

def set_value_into_element(driver, locator, selector, value):
    element = get_element(driver, locator, selector)
    element.send_keys(value)

def set_keywords_filter(driver, keywords):
    selector = "keywords-input"
    set_value_into_element(driver, By.ID, selector, keywords)

def set_location_filter(driver, location):
    selector = "SearchBar__Where"
    set_value_into_element(driver, By.ID, selector, location)

def search_jobs(driver):
    selector = "searchButton"
    click_element_by_id(driver, selector)

def set_job_filters(driver, keywords, location, time="Today", classification_id="6281", sorted_by="sortby-1"):
    set_keywords_filter(driver, keywords)
    set_location_filter(driver, location)

    search_jobs(driver)
    
    set_listing_time_radio(driver, time)
    set_classification_checkbox(driver, classification_id)
    set_sorted_by(driver, sorted_by)

def get_jobs_by_page(driver, page_number):
    jobs_by_page = []
    limit_of_jobs_per_page = 23
    for card_index in range(1, limit_of_jobs_per_page):
        card = get_next_job_card(driver, card_index)
        if card == None:
            break
        
        card_id = get_attribute_from_element(card, "data-job-id")
        card_title = get_attribute_from_element(card, "aria-label")

        job_details = get_job_ad_details_element(driver, card_id)
        job_description = get_text_from_element(job_details)

        print(f"Page: {page_number} Job Number: {card_index} Job Title: {card_title}")
        card_info = get_job_info(driver, card_id, card_title, job_description)
        jobs_by_page.append(card_info)

    return jobs_by_page

def get_all_jobs(driver, number_of_jobs):
    job_list = []
    page_number = 1
    while True:
        jobs_by_page = get_jobs_by_page(driver, page_number)
        job_list.extend(jobs_by_page)

        if len(job_list) >= number_of_jobs:
            return job_list
        
        page_number += 1
        page = get_next_job_page(driver, page_number)
        if not page:
            break

        click_element(driver, page)
        time.sleep(1)

    return job_list

def get_job_list_applying_additional_filters(driver, work_type, number_of_jobs):
    jobs_filtered = []
    job_list = get_all_jobs(driver, number_of_jobs)

    for job in job_list:
        if is_job_matches_with_additional_filters(work_type, job["description"], job["title"]):
            jobs_filtered.append({
                "id": job["id"],
                "title": job["title"],
                "href" : job["href"]
            })
    
    return jobs_filtered