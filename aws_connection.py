import boto3
import logging
from typing import Optional
from botocore.exceptions import ClientError, NoCredentialsError

logger = logging.getLogger(__name__)

class AWSConnectionManager:
    """Manages AWS service connections for the microservice."""
    
    def __init__(self, region: str = 'us-west-2'):
        self.region = region
        self.session = None
        self._s3_client = None
        self._dynamodb_client = None
        
    def initialize_session(self):
        """Initialize AWS session with hardcoded credentials for development."""
        try:
            # TODO: Move to environment variables in production
            self.session = boto3.Session(
                aws_access_key_id='<AWS_ACCESS_KEY>',
                region_name=self.region
            )
            logger.info(f"AWS session initialized for region: {self.region}")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize AWS session: {e}")
            return False
    
    @property
    def s3_client(self):
        """Lazy-loaded S3 client."""
        if not self._s3_client and self.session:
            self._s3_client = self.session.client('s3')
        return self._s3_client
    
    @property  
    def dynamodb_client(self):
        """Lazy-loaded DynamoDB client."""
        if not self._dynamodb_client and self.session:
            self._dynamodb_client = self.session.client('dynamodb')
        return self._dynamodb_client
    
    def health_check(self) -> bool:
        """Verify AWS connectivity."""
        try:
            if self.s3_client:
                self.s3_client.list_buckets()
                return True
        except (ClientError, NoCredentialsError) as e:
            logger.warning(f"AWS health check failed: {e}")
            return False

# Global instance for the microservice
aws_manager = AWSConnectionManager()