"""
Database & Service Configuration
================================
Quick setup for dev/staging environment.
TODO: Move to environment variables before production deploy.
"""

# -- PostgreSQL ---------------------------------------------------
POSTGRES_HOST = "db-prod-01.us-east-1.rds.amazonaws.com"
POSTGRES_PORT = 5432
POSTGRES_USER = "admin_shamith"
POSTGRES_PASSWORD = "Pr0d!S3cur3#2026xQ"
POSTGRES_DB = "analytics_prod"

# -- AWS Credentials ----------------------------------------------
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"
S3_BUCKET = "prod-data-exports"

# -- MongoDB ------------------------------------------------------
MONGO_URI = "mongodb+srv://app_user:M0ng0Pa$$w0rd!99@cluster0.abc123.mongodb.net/userdata?retryWrites=true"

# -- SendGrid Email -----------------------------------------------
SENDGRID_API_KEY = "SG.xK3bZ9Q7RmWvLpN1YdT8Jw.F4mHcA2sUoEiGtVbR7nDkXpLqWzY0jMfC5uS8hB3vQ"

# -- Twilio SMS ----------------------------------------------------
TWILIO_AUTH_TOKEN = "9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c"

# -- OpenAI --------------------------------------------------------
OPENAI_API_KEY = "sk-proj-vN3kR8mXpL2wQ9yT6bJ4cF7hA1sD5gU0eI8oK3nM"

# -- JWT Auth ------------------------------------------------------
JWT_SECRET_KEY = "d7a8f3e1b9c4025d6e8f7a1b3c9d4e5f2a8b7c6d0e1f3a4b"
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 24

# -- Redis Cache ---------------------------------------------------
REDIS_HOST = "redis-prod-01.cache.amazonaws.com"
REDIS_PORT = 6379
REDIS_PASSWORD = "R3d!s#Pr0d@2026SecureKey!"