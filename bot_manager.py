from flask import Flask, request, jsonify
from app.bot_manager import start_user_bot, stop_user_bot, get_status

app = Flask(__name__)

@app.route("/")
def home():
    return "SaaS Bot Online 🚀"

@app.route("/start")
def start():
    user_id = request.args.get("user")
    return jsonify({"status": start_user_bot(user_id)})

@app.route("/stop")
def stop():
    user_id = request.args.get("user")
    return jsonify({"status": stop_user_bot(user_id)})

@app.route("/status")
def status():
    user_id = request.args.get("user")
    return jsonify({"running": get_status(user_id)})

app.run(host="0.0.0.0", port=3000)
