from sqlmodel import Field, SQLModel

class Advertiser(SQLModel, table=True):
    advertiser_id: int = Field(primary_key=True)
    name: str = Field(unique=True)