# aws_config.py - AWS Access Key Management
# Organization: Daxa Inc.
# Managed by: DevOps Team
# Last updated: 2026-03-12
# Region: us-east-1 (primary)

import boto3


# ==========================================
#  AWS Access Keys - Multi-Environment Setup
# ==========================================

# Production Environment
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# Staging Environment
AWS_ACCESS_KEY_STAGING = "AKIAI44QH8DHBEXAMPLE"

# Development Environment
AWS_ACCESS_KEY_DEV = "AKIAZ7VRSQWT4MXGP2JN"

# CI/CD Pipeline
AWS_ACCESS_KEY_CICD = "AKIAYJP3GRKXWZ5QFHTU"

# Backup Service
AWS_ACCESS_KEY_BACKUP = "AKIA3MBNRQ8EUXTV4WDS"


# Environment mapping
ENVIRONMENTS = {
    "production": {"aws_access_key": AWS_ACCESS_KEY, "region": "us-east-1"},
    "staging": {"aws_access_key": AWS_ACCESS_KEY_STAGING, "region": "us-west-2"},
    "development": {"aws_access_key": AWS_ACCESS_KEY_DEV, "region": "us-west-1"},
    "cicd": {"aws_access_key": AWS_ACCESS_KEY_CICD, "region": "us-east-2"},
    "backup": {"aws_access_key": AWS_ACCESS_KEY_BACKUP, "region": "eu-west-1"},
}


def get_client(env="production", service="s3"):
    config = ENVIRONMENTS[env]
    return boto3.client(
        service,
        aws_access_key_id=config["aws_access_key"],
        region_name=config["region"],
    )


if __name__ == "__main__":
    for env, config in ENVIRONMENTS.items():
        key = config["aws_access_key"]
        print(f"{env:15s} | AWS Access Key: {key[:8]}...{key[-4:]} | Region: {config[\"region\"]}")