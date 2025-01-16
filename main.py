from flask import Flask, request, jsonify
import unicodedata
import os

app = Flask(__name__)

# Home route to verify the API is running
@app.route('/')
def home():
    return "Text Normalization API is running!"

# Normalization endpoint
@app.route('/normalize', methods=['POST'])
def normalize_text():
    # Parse the input JSON data
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400
    
    # Get the input text
    fonted_text = data['text']
    
    # Normalize the text: remove special fonts and accents
    normalized_text = ''.join(
        c for c in unicodedata.normalize('NFKD', fonted_text) if not unicodedata.combining(c)
    )
    
    # Return the normalized text
    return jsonify({"normalized_text": normalized_text})

# Run the Flask app
if __name__ == '__main__':
    # Use PORT environment variable if running on Render or Replit
import os

    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
