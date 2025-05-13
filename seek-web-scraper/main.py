import logging
from classes.amazon_s3 import AmazonS3Storage
from classes.db import WebScrapingDB
from classes.seek_web_scraping import SeekWebScraping
from utils.lib import get_event_data, get_response
from utils.models import Filters

amazon_s3 = AmazonS3Storage()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_seek_jobs(filters: Filters, additional_filters: list[str]):
    seek = SeekWebScraping()
    seek.set_filters(filters)
    job_list = seek.get_jobs(additional_filters)
    seek.quit()
    return job_list

def save_result_into_database(save_result: bool, job_list: list):
    message = "Jobs processed successfully.",
    if not (save_result and job_list):
        return "No jobs found." if not job_list else "Jobs processed successfully, but not saved."
    
    database = WebScrapingDB()
    database.save_all_jobs(job_list)
    database.close()
    
    amazon_s3.upload_file()

    return message
        
def handler(event, context):
    try:
        data = get_event_data(event)
        amazon_s3.download_file()
        
        job_list = get_seek_jobs(data.filters, data.additional_filters)
        message = save_result_into_database(data.save_result, job_list)
        
        amazon_s3.close()
        return get_response(200, {"message": message, "jobs": job_list}) 
    except Exception as e:
        logger.exception("Error processing Lambda event")
        return get_response(500, {"error": str(e)})
    
event = {
  "filters": {
    "keywords": "Software Engineer",
    "location": "All Sydney NSW",
    "time": "Today",
    "classification": "6281",
    "sort": "sortby-1"
  },
  "additional_filters": ["part-time", "part time", " intern ", "internship", "sponsorship", "sponsor"],
  "save_result": True,
  "return_result": True
}

context = {}
print(handler(event, context))