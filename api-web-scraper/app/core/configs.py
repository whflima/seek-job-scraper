from typing import ClassVar
from pydantic_settings import BaseSettings


class Configs(BaseSettings):
    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # database
    DATABASE_URL: ClassVar[str] = "sqlite:///./web_scraping.db"

    class Config:
        case_sensitive = True

configs = Configs()