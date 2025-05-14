from app.repository.job_repository import JobRepository
from app.dependencies.job_filters import JobFilters
from app.dependencies.pagination_params import PaginationParams

class JobService():
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository
    
    def get_all(self):
        return self.job_repository.get_all()
    
    def get_job(self, filters: JobFilters, pagination: PaginationParams):
        return self.job_repository.get_job(filters, pagination)