# app.py
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Ensure you set this in .env file

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.json
    keywords = data.get('keywords')
    audience = data.get('audience')
    tone = data.get('tone')

    prompt = f"Generate a social media post for {audience} with a {tone} tone about {keywords}."

    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
        json={
            'prompt': prompt,
            'max_tokens': 100
        }
    )

    result = response.json()
    generated_text = result['choices'][0]['text'].strip()

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
