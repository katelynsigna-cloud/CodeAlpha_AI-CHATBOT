from flask import Flask, request, jsonify,render_template

import json
import random

app = Flask(__name__)

with open("intents.json") as file:
    data = json.load(file)
@app.route("/")    
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in user_message:

                return jsonify({
                    "response":
                    random.choice(intent["responses"])
                })

    return jsonify({
        "response":
        data["intents"][-1]["responses"][0]
    })

if __name__ == "__main__":
    app.run(debug=True)
