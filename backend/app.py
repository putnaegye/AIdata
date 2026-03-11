from flask import Flask, request, jsonify
from chatbot_logic import get_reply

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    reply = get_reply(message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
