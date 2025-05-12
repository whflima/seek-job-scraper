from pydantic import BaseModel


class JobSchema(BaseModel):
    job_id: int
    advertiser_id: int
    title: str
    link: str
    created_at: str
    
    class Config:
        orm_mode = True