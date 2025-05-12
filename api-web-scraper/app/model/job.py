from sqlmodel import Field, SQLModel

class Job(SQLModel, table=True):
    __tablename__ = "job"
    job_id: int = Field(primary_key=True)
    advertiser_id: int = Field(foreign_key="advertiser.advertiser_id")
    title: str = Field(unique=False)
    link: str = Field(unique=False)
    created_at: str = Field(unique=False)