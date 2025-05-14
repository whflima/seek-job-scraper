from app.model.job import Job
from app.schema.job_schema import JobSchema

def convert_single_job_to_schema(job: Job) -> JobSchema:
    """
    Converts a Job ORM object to a Pydantic JobSchema,
    extracting advertiser_name from the related Advertiser object.
    """
    return JobSchema(
        job_id=job.job_id,
        title=job.title,
        link=job.link,
        created_at=job.created_at,
        advertiser_name=job.advertiser.name if job.advertiser else None
    )

def convert_jobs_to_schema(jobs: list[Job]) -> list[JobSchema]:
    """
    Converts a list of Job ORM objects to a list of JobSchema objects.
    """
    return [convert_single_job_to_schema(job) for job in jobs]