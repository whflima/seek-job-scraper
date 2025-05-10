import os
from pathlib import Path
import tempfile
from typing import ClassVar
from pydantic_settings import BaseSettings

from app.utils.s3_utils import download_db_from_s3

class Configs(BaseSettings):
    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    S3_BUCKET: str= "s3-seek-job-scraper-bucket"
    S3_KEY: str = "web_scraping.db"
    TEMP_DIR: str = tempfile.gettempdir()
    DEST: str = os.path.join(TEMP_DIR, 'web_scraping.db')

    # database
    db_path: str = download_db_from_s3(bucket=S3_BUCKET, key=S3_KEY, dest=DEST)
    DATABASE_URL: str = f"sqlite:///{db_path}"

    class Config:
        case_sensitive = True

configs = Configs()