# secrets_test.py - Multi-Service Credential Store
# Organization: Daxa Inc.
# Managed by: DevOps Team
# Last updated: 2026-03-12


# ==========================================
#  AWS Access Keys
# ==========================================
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_ACCESS_KEY_STAGING = "AKIAI44QH8DHBEXAMPLE"
AWS_ACCESS_KEY_DEV = "AKIAZ7VRSQWT4MXGP2JN"
AWS_ACCESS_KEY_CICD = "AKIAYJP3GRKXWZ5QFHTU"
AWS_ACCESS_KEY_BACKUP = "AKIA3MBNRQ8EUXTV4WDS"

# ==========================================
#  GitHub Tokens
# ==========================================
GITHUB_TOKEN = "ghp_R4nD0mT0k3nV4lu3X9kLmNpQrStUvWxYz12"
GITHUB_TOKEN_FINEGRAINED = "github_pat_11ABCDEF0_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789AbCdEfGhIjKlMnOpQr"
GITHUB_TOKEN_OAUTH = "gho_16C7e42F292c6912E7710c838347Ae178B4a"
GITHUB_TOKEN_USER = "ghu_ABCDEFabcdef1234567890ABCDEF1234abcd"
GITHUB_TOKEN_SERVER = "ghs_1234ABCDefgh5678ijklMNOP9012qrstUVWX"

# ==========================================
#  Azure Keys
# ==========================================
AZURE_CLIENT_ID = "8a3b5c7d-9e1f-4a2b-8c3d-5e6f7a8b9c0d"
AZURE_CLIENT_SECRET = "Knx8Q~2mRfHb.Lp9TvWz3XyA5jCdEgHiJkMnOpQr"
AZURE_TENANT_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
AZURE_SUBSCRIPTION_KEY = "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
AZURE_STORAGE_KEY = "eJwdj8FqwzAMhl9FNxA7DhO3MugO4yxQ3frQViK4uDYLpbTsVQ=="


SERVICES = {
    "aws": [AWS_ACCESS_KEY, AWS_ACCESS_KEY_STAGING, AWS_ACCESS_KEY_DEV, AWS_ACCESS_KEY_CICD, AWS_ACCESS_KEY_BACKUP],
    "github": [GITHUB_TOKEN, GITHUB_TOKEN_FINEGRAINED, GITHUB_TOKEN_OAUTH, GITHUB_TOKEN_USER, GITHUB_TOKEN_SERVER],
    "azure": [AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_KEY, AZURE_STORAGE_KEY],
}


if __name__ == "__main__":
    for service, keys in SERVICES.items():
        print(f"\n{service.upper()}:")
        for i, key in enumerate(keys, 1):
            print(f"  Key {i}: {str(key)[:12]}...")
