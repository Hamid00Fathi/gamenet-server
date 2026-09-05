from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


db = {}   # ذخیرهٔ وضعیت کاربران

@app.route("/update/<username>", methods=["POST"])
def update(username):
    db[username] = request.json
    return jsonify({"status": "ok"})

@app.route("/status/<username>", methods=["GET"])
def status(username):
    return jsonify(db.get(username, {}))

