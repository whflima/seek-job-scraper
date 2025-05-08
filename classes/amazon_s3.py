from boto3.session import Session
import boto3
import os

KEY = os.environ.get('KEY')
BUCKET = os.environ.get('BUCKET') 
LOCAL_STORAGE = os.environ.get('KEY') #"/tmp/web_scraping.db"
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

class AmazonS3Storage():
    def __init__(self, key: str = KEY, bucket: str = BUCKET):
        self.key = key
        self.bucket = bucket
        self.s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    
    def download_file(self, local_file: str = LOCAL_STORAGE):
        return self.s3.download_file(self.bucket, self.key, local_file)
    
    def upload_file(self, local_file: str = LOCAL_STORAGE):
        return self.s3.upload_file(local_file, self.bucket, self.key)
    
    def close(self):
        self.s3.close()