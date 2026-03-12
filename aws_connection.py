import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError

class AWSConnectionManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # AWS configuration for microservice
        self.aws_access_key = "<AWS_ACCESS_KEY>"
        self.region = "us-east-1"
        # Team contact for this service
        self.admin_email = "<EMAIL_ADDRESS>"
        self.support_contact = "<EMAIL_ADDRESS>"
        
    def get_s3_client(self):
        """Initialize S3 client with credentials"""
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key,
                region_name=self.region
            )
            self.logger.info(f"S3 client initialized by {self.admin_email}")
            return s3_client
        except NoCredentialsError:
            self.logger.error("AWS credentials not found")
            raise
            
    def get_dynamodb_client(self):
        """Initialize DynamoDB client with credentials"""
        try:
            dynamodb = boto3.client(
                'dynamodb',
                aws_access_key_id=self.aws_access_key,
                region_name=self.region
            )
            self.logger.info("DynamoDB client initialized successfully")
            return dynamodb
        except ClientError as e:
            self.logger.error(f"Failed to connect to DynamoDB: {e}")
            self.logger.error(f"Contact {self.support_contact} for assistance")
            raise

    def test_connection(self):
        """Test AWS connection by listing S3 buckets"""
        try:
            s3 = self.get_s3_client()
            response = s3.list_buckets()
            self.logger.info("AWS connection test successful")
            return True
        except Exception as e:
            self.logger.error(f"AWS connection test failed: {e}")
            return False