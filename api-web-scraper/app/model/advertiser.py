from typing import List
from sqlmodel import Field, Relationship, SQLModel

class Advertiser(SQLModel, table=True):
    advertiser_id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    
    jobs: List["Job"] = Relationship(back_populates="advertiser")