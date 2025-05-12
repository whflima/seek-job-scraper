from pydantic import BaseModel


class StackSchema(BaseModel):
    tech_stack_id: int
    category: str
    subcategory: str
    stack: str
    created_at: str
    
    class Config:
        orm_mode = True