import sqlite3
from utils.schema_sql import (
    query_create_website_provider_table,
    query_create_advertiser_table,
    query_create_website_provider_advertiser_table,
    query_create_job_table,
    query_create_tech_stack_table,
    query_create_job_tech_stack_table,
    query_insert_website_provider_table,
    query_insert_advertiser_table,
    query_insert_website_provider_advertiser_table,
    query_insert_job_table,
    query_insert_tech_stack_table,
    query_insert_job_tech_stack_table,
    query_select_get_advertiser_id,
    query_select_get_website_provider_id,
    query_select_get_tech_stack_id
)
from utils.models import Advertiser, Job, JobCard, JobTechStack, TechStack, WebsiteProvider, WebsiteProviderAdvertiser
from utils.types import Parameters


class WebScrapingDB:
    
    def __init__(self, db_path: str = "web_scraping.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(query_create_website_provider_table)
        cursor.execute(query_create_advertiser_table)
        cursor.execute(query_create_website_provider_advertiser_table)
        cursor.execute(query_create_job_table)
        cursor.execute(query_create_tech_stack_table)
        cursor.execute(query_create_job_tech_stack_table)
        self.connection.commit()
    
    def _execute_insert(self, sql: str, parameters: Parameters = ()):
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters)
        self.connection.commit()
        return cursor.lastrowid
    
    def _execute_select(self, sql: str, parameters: Parameters = ()):
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters)
        return cursor.fetchone()[0]
    
    def insert_website_provider(self, provider: WebsiteProvider) -> int:
        return self._execute_insert(query_insert_website_provider_table, (provider.name,))
    
    def insert_advertiser(self, advertiser: Advertiser) -> int:
        return self._execute_insert(query_insert_advertiser_table, (advertiser.name,))
    
    def insert_job(self, job: Job) -> int:
        return self._execute_insert(query_insert_job_table, (job.advertiser_id, job.title, job.link,))
    
    def insert_tech_stack(self, techStack: TechStack) -> int:
        return self._execute_insert(query_insert_tech_stack_table, (techStack.category, techStack.subcategory, techStack.stack, ))
    
    def link_website_provider_advertiser(self, provider_advertiser: WebsiteProviderAdvertiser) -> int:
        return self._execute_insert(
            query_insert_website_provider_advertiser_table, 
            (provider_advertiser.website_provider_id, provider_advertiser.advertiser_id,))
        
    def link_job_tech_stack(self, jobTechStack: JobTechStack) -> int:
        return self._execute_insert(query_insert_job_tech_stack_table, (jobTechStack.job_id, jobTechStack.tech_stack_id,))
    
    def get_tech_stack_id(self, tech_stack: TechStack):
        return self._execute_select(query_select_get_tech_stack_id, (tech_stack.category, tech_stack.subcategory, tech_stack.stack,))
    
    def get_website_provider_id(self, website_provider: str):
        return self._execute_select(query_select_get_website_provider_id, (website_provider,))
    
    def get_advertiser_id(self, advertiser: str):
        return self._execute_select(query_select_get_advertiser_id, (advertiser,))
    
    def save_tech_stacks(self, job_id, stacks: list[TechStack]):
        for stack in stacks:
            self.insert_tech_stack(stack)
            tech_stack_id = self.get_tech_stack_id(stack)
            self.link_job_tech_stack(JobTechStack(job_id, tech_stack_id))
    
    def save_job(self, job_card: JobCard, website_provider: str = "Seek"):
        self.insert_website_provider(WebsiteProvider(name=website_provider))
        self.insert_advertiser(job_card.advertiser)
        
        website_provider_id = self.get_website_provider_id(website_provider)
        advertiser_id = self.get_advertiser_id(job_card.advertiser.name,)
        self.link_website_provider_advertiser(WebsiteProviderAdvertiser(advertiser_id, website_provider_id))
        
        job_card.job.advertiser_id = advertiser_id
        job_id = self.insert_job(job_card.job)
        self.save_tech_stacks(job_id, job_card.stacks)
        
    
    def save_all_jobs(self, jobs: list):
        for job in jobs:
            self.save_job(job)
    
    def close(self):
        self.connection.close()