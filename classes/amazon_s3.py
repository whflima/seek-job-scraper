from boto3.session import Session
import boto3
import os

KEY = os.environ.get('AWS_FILE_BUCKET_KEY')
BUCKET = os.environ.get('AWS_BUCKET_NAME') 
REGION = os.environ.get('REGION')
LOCAL_STORAGE = "web_scraping.db" #os.environ.get('KEY') "/tmp/web_scraping.db"

class AmazonS3Storage():
    def __init__(self, key: str = KEY, bucket: str = BUCKET):
        self.key = key
        self.bucket = bucket
        self.s3 = boto3.client('s3', region_name=REGION)
    
    def download_file(self, local_file: str = LOCAL_STORAGE):
        return self.s3.download_file(self.bucket, self.key, local_file)
    
    def upload_file(self, local_file: str = LOCAL_STORAGE):
        return self.s3.upload_file(local_file, self.bucket, self.key)
    
    def close(self):
        self.s3.close()