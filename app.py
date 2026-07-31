from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_KEYS = {
    "VIP-12345": {
        "type": "VIP",
        "token": "التوكن_الحقيقي_هنا"
    }
}

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.json
    user_key = data.get("key")

    if user_key in VALID_KEYS:
        return jsonify({
            "status": "success",
            "type": VALID_KEYS[user_key]["type"],
            "token": VALID_KEYS[user_key]["token"]
        })
    else:
        return jsonify({"status": "error", "message": "Invalid Key"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)