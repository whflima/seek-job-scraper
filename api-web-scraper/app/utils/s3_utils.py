import os

import boto3

def delete_file_if_exists(filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    os.remove(filepath)
    print(f"Deleted file: {filepath}")
    
def download_db_from_s3(bucket: str, key: str, dest: str = "/tmp/web_scraping.db"):
    delete_file_if_exists(dest)
    
    s3 = boto3.client("s3")
    s3.download_file(bucket, key, dest)
    print(f"SQLite DB downloaded to {dest}")
    return dest