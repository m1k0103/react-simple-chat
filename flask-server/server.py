from flask import Flask, jsonify
import os


app = Flask(__name__)


@app.route("/send_chat", methods=["POST"])
def send_chat():
    pass

@app.route("/get_chats")
def get_chats():
    with open("chats.txt", "r") as c:
        contents = list(c.readlines())
        all_chats = {"chats":[]}
        for el in contents: # sender | message
            sender, message = el.split(" | ")
            all_chats["chats"].append({sender:message})
    print(all_chats)
    return jsonify(all_chats)

if __name__ == "__main__":
    print(os.chdir("flask-server"))
    app.run(debug=True)