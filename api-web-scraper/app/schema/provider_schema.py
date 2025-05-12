from pydantic import BaseModel


class ProviderSchema(BaseModel):
    website_provider_id: int
    created_at: str
    name: str
    
    class Config:
        orm_mode = True