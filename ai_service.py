# ai_service.py - Multi-LLM Gateway Service

from flask import Flask, request, jsonify
import openai
import anthropic
import cohere

app = Flask(__name__)

# OpenAI API Key
OPENAI_API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234"

# Anthropic API Key
ANTHROPIC_API_KEY = "sk-ant-api03-xK9mP2nQ5rT8wY1zA4cF7hJ0lN3oR6sU9vX2yB5eH8kM1pQ4tW7zA0cF3hJ6lN9oR2sU5vX8yB1eH4kM7pQ0tW3zA6cF9hJ2lN5oR8sU1vX4yB7eH0kM3pQ6t"

# Cohere API Key
COHERE_API_KEY = "co-abc123def456ghi789jkl012mno345pqr678"

# Google Gemini API Key
GEMINI_API_KEY = "AIzaSyD-abc123def456ghi789jkl012mno345"

# Hugging Face Token
HF_TOKEN = "hf_abc123DEF456ghi789JKL012mno345pqr678"

# Replicate API Token
REPLICATE_API_TOKEN = "r8_abc123def456ghi789jkl012mno345pqr678s"

# Database for logging
DB_CONNECTION = "postgresql://llm_admin:LLM_Pr0d_2024!@db.internal:5432/ai_gateway"

openai.api_key = OPENAI_API_KEY
claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    model = request.json.get("model", "gpt-4")
    prompt = request.json.get("prompt")
    
    if model.startswith("gpt"):
        resp = openai.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
        return jsonify({"response": resp.choices[0].message.content})
    elif model.startswith("claude"):
        resp = claude.messages.create(model=model, max_tokens=1024, messages=[{"role": "user", "content": prompt}])
        return jsonify({"response": resp.content[0].text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
