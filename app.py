from flask import Flask, render_template,request, jsonify
import requests


app = Flask(__name__)
API_KEY = "PASTE-YOUR-API-KEY"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-response', methods=['POST'])
def generate_response():
    chat_history = request.json.get('contents', [])
    try:
        response = requests.post(API_URL, json={'contents': chat_history})
        response.raise_for_status()
        data = response.json()
        response_text = data['candidates'][0]['content']['parts'][0]['text'].replace('**', '').strip()
        return jsonify({'text': response_text})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

