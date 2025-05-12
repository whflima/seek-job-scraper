from app.repository.job_repository import JobRepository

class JobService():
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository
    
    def get_all(self):
        return self.job_repository.get_all()