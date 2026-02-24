# app.py - User Analytics Service

from flask import Flask, jsonify
import pymongo
import requests

app = Flask(__name__)

# MongoDB Production Database
MONGO_URI = "mongodb://admin:Pr0duction_P@ssw0rd!@10.0.1.45:27017/analytics_prod"

# Internal API Gateway Token
API_GATEWAY_TOKEN = "gw-tok-9f84a2c1e67b430d8e1f5a2b7c9d3e6f"

# Encryption Key for user PII data
PII_ENCRYPTION_KEY = "aes-256-cbc:8kF3mN9pQ2wX5vB7jL4hR1tY6uI0oA3s"

# Admin Dashboard Credentials
ADMIN_USERNAME = "superadmin"
ADMIN_PASSWORD = "Change_Me_N3ver!2024"

# SendGrid Email API
SENDGRID_KEY = "SG.internal.dkf93hf8h2f98h23f98h2398fh"

# Redis Cache (production)
REDIS_URL = "redis://:CacheP@ss_Prod_2024@redis-prod.internal:6379/0"

client = pymongo.MongoClient(MONGO_URI)
db = client.analytics_prod

@app.route("/users")
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/notify")
def notify():
    headers = {"Authorization": f"Bearer {API_GATEWAY_TOKEN}"}
    resp = requests.post("https://api.internal/notify", headers=headers)
    return jsonify({"status": resp.status_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
