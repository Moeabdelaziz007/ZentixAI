from flask import Flask, request, jsonify
from zero_system import ZeroSystem
import os
import requests

app = Flask(__name__)

# Reuse a single ZeroSystem instance for all requests
system = ZeroSystem()

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json(force=True) or {}
    message = data.get('message')
    user_profile = data.get('user_profile')
    if not message:
        return jsonify({'error': 'message is required'}), 400

    response = system.interact(message, user_profile)

    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        payload = {
            'contents': [{'role': 'user', 'parts': [{'text': message}]}]
        }
        try:
            r = requests.post(f"{GEMINI_URL}?key={api_key}", json=payload, timeout=10)
            if r.ok:
                data = r.json()
                content = data.get('candidates', [{}])[0].get('content', {})
                gemini_text = content.get('parts', [{}])[0].get('text')
                if gemini_text:
                    response['gemini'] = gemini_text
        except Exception as exc:
            response['gemini_error'] = str(exc)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
