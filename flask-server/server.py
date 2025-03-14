from flask import Flask, jsonify, request
import os


app = Flask(__name__)


@app.route("/send_message",methods=["POST"])
def send_chat():
    contents = request.get_json()
    print(contents)
    if contents["sender"]["username"] == '':
        return {"action":"fail"}
    
    with open("flask-server/chats.txt", "a") as c:
        c.write(f"{contents["sender"]["username"]} | {contents["message"]["new_message"]}\n")
    return {"action":"success"}

@app.route("/get_chats")
def get_chats():
    #opens chats file
    with open("flask-server/chats.txt", "r") as c:
        contents = list(c.readlines())
        all_chats = {"chats": []}
        for el in contents: # sender | message
            sender, message = el.split(" | ")
            all_chats["chats"].append({"sender":sender, "message":message.strip("\n")})
    print(all_chats)
    return jsonify(all_chats)

if __name__ == "__main__":
    app.run(debug=True)