from sqlmodel import Field, SQLModel

class Stack(SQLModel, table=True):
    __tablename__ = "tech_stack"
    tech_stack_id: int = Field(primary_key=True)
    category: str = Field(unique=False)
    subcategory: str = Field(unique=False)
    stack: str = Field(unique=False)
    created_at: str = Field(unique=False)