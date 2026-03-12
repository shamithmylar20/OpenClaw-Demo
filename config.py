# config.py - Cloud Service Configuration
# Environment: Production
# Last updated: 2026-03-12
# Format testing for security scanning

import os

# ============================================
# GITHUB TOKENS - Various Formats
# ============================================
GITHUB_TOKEN_V1 = "ghp_R4nD0mT0k3nV4lu3X9kLmNpQrStUvWxYz12"
GITHUB_TOKEN_V2 = "github_pat_11ABCDEF0_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789AbCdEfGhIjKlMnOpQr"
GITHUB_TOKEN_V3 = "gho_16C7e42F292c6912E7710c838347Ae178B4a"
GITHUB_TOKEN_V4 = "ghu_ABCDEFabcdef1234567890ABCDEF1234abcd"
GITHUB_TOKEN_V5 = "ghs_1234ABCDefgh5678ijklMNOP9012qrstUVWX"

# ============================================
# AWS ACCESS KEYS - Various Formats
# ============================================
AWS_KEY_V1 = "AKIAIOSFODNN7EXAMPLE"
AWS_KEY_V2 = "AKIAI44QH8DHBEXAMPLE"
AWS_KEY_V3 = "ASIAJEXAMPLEXEG2JICEA"
AWS_KEY_V4 = "ANPAJ2UCCR6DPCEXAMPLE"
AWS_KEY_V5 = "AROA3XFRBF23OW56KEXAM"

# ============================================
# AZURE CREDENTIALS - Various Formats
# ============================================
AZURE_CLIENT_ID_V1 = "8a3b5c7d-9e1f-4a2b-8c3d-5e6f7a8b9c0d"
AZURE_CLIENT_SECRET_V1 = "Knx8Q~2mRfHb.Lp9TvWz3XyA5jCdEgHiJkMnOpQr"
AZURE_TENANT_V1 = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
AZURE_SUBSCRIPTION_KEY = "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
AZURE_STORAGE_KEY = "eJwdj8FqwzAMhl9F+NxA7DhO3MugO4yxQ3frQViK4uDYLpbTsVQ=="


def load_config():
    return {
        "github": [GITHUB_TOKEN_V1, GITHUB_TOKEN_V2, GITHUB_TOKEN_V3, GITHUB_TOKEN_V4, GITHUB_TOKEN_V5],
        "aws": [AWS_KEY_V1, AWS_KEY_V2, AWS_KEY_V3, AWS_KEY_V4, AWS_KEY_V5],
        "azure": [AZURE_CLIENT_ID_V1, AZURE_CLIENT_SECRET_V1, AZURE_TENANT_V1, AZURE_SUBSCRIPTION_KEY, AZURE_STORAGE_KEY],
    }


if __name__ == "__main__":
    config = load_config()
    for service, keys in config.items():
        print(f"\n{service.upper()}:")
        for i, key in enumerate(keys, 1):
            print(f"  V{i}: {key[:10]}...{key[-4:]}")