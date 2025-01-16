from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/normalize', methods=['POST'])
def normalize():
    data = request.json
    if data and "text" in data:
        input_text = data["text"]
        normalized_text = ''.join(c for c in input_text if c.isalnum() or c.isspace())
        return jsonify({"normalized": normalized_text})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
