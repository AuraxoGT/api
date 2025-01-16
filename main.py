from flask import Flask, request, jsonify
import unicodedata

app = Flask(__name__)

def normalize_text(text):
    # Normalize the text to NFKD form and filter out non-standard characters
    normalized = unicodedata.normalize("NFKD", text)
    return ''.join(c for c in normalized if c.isascii())

@app.route('/normalize', methods=['POST'])
def normalize():
    data = request.json
    if data and "text" in data:
        input_text = data["text"]
        normalized_text = normalize_text(input_text)
        return jsonify({"normalized": normalized_text})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
