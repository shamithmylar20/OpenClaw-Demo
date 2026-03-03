# Cloud Infrastructure Configuration
# Author: Junior Dev
# Date: 2026-03-03

import boto3

# AWS Configuration
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"
S3_BUCKET = "company-internal-data"

# GitHub Personal Access Token for CI/CD
GITHUB_TOKEN = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef12"

# Initialize AWS session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

s3_client = session.client("s3")

def upload_to_s3(file_path, key):
    s3_client.upload_file(file_path, S3_BUCKET, key)
    print(f"Uploaded {file_path} to s3://{S3_BUCKET}/{key}")

def get_github_repos():
    import requests
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get("https://api.github.com/user/repos", headers=headers)
    return resp.json()