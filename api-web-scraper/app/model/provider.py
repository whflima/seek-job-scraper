from sqlmodel import Field, SQLModel

class Provider(SQLModel, table=True):
    __tablename__ = "website_provider"
    website_provider_id: int = Field(primary_key=True)
    created_at: str = Field(unique=False)
    name: str = Field(unique=True)