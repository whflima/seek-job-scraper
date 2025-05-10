from pydantic import BaseModel


class AdvertiserSchema(BaseModel):
    advertiser_id: int
    name: str
    
    class Config:
        orm_mode = True