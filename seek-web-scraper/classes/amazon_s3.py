import tempfile
import boto3
import os

KEY = os.environ.get('AWS_FILE_BUCKET_KEY')
BUCKET = os.environ.get('AWS_BUCKET_NAME') 
REGION = os.environ.get('REGION')
TEMP_DIR: str = tempfile.gettempdir()
LOCAL_STORAGE: str = os.path.join(TEMP_DIR, 'web_scraping.db')

class AmazonS3Storage():
    def __init__(self, key: str = KEY, bucket: str = BUCKET):
        self.key = key
        self.bucket = bucket
        self.s3 = boto3.client('s3', region_name=REGION)
    
    def _delete_file(self, local_file: str):
        os.makedirs(os.path.dirname(local_file), exist_ok=True)
        if not os.path.exists(local_file):
            print(f"File not found: {local_file}")
            return
        
        os.remove(local_file)
        print(f"Deleted file: {local_file}")
        
    def download_file(self, local_file: str = LOCAL_STORAGE):
        self._delete_file(local_file)
        self.s3.download_file(self.bucket, self.key, local_file)
        return LOCAL_STORAGE
    
    def upload_file(self, local_file: str = LOCAL_STORAGE):
        return self.s3.upload_file(local_file, self.bucket, self.key)
    
    def close(self):
        self._delete_file(LOCAL_STORAGE)
        self.s3.close()