from flask import Flask, request
app = Flask(__name__)

db = {}

@app.route("/update/<gamenet_id>", methods=["POST"])
def update(gamenet_id):
    db[gamenet_id] = request.json
    return {"status": "ok"}

@app.route("/status/<gamenet_id>", methods=["GET"])
def status(gamenet_id):
    return db.get(gamenet_id, {})