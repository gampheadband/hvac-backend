from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app) # This allows your website to talk to this script

# We will set this key in Render later for security
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message")
    
    prompt = (
        "You are a professional HVAC dispatcher. Be helpful and brief. "
        "Your goal is to get the customer's Name, Phone Number, and a description of their issue. "
        "Ask only one question at a time. "
        f"User says: {user_input}"
    )
    
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
