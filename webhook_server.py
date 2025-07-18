from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/github-webhook/', methods=['POST'])
def webhook():
    print("✅ Webhook received:", request.json)
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=8000)
