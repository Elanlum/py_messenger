import json
import uuid

from flask import Flask, request, abort, render_template
import time
import datetime

app = Flask(__name__)


@app.route("/")
def index_page():
    return "HELLO"

db = []

db_file = ".././data/db.json"
# json_db = open(db_file, "rb")
# data = json.load(json_db)
# db = data["messages"]
with open(db_file, "rb") as json_db:
    data = json.load(json_db)
    db = data["messages"]

def save_messages():
    data = {
        "messages": db
    }
    json_db = open(db_file, "w")
    json.dump(data, json_db)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/sendMessage", methods=['POST'])
def send_message():
    # if request.method == 'POST':
    #     return "POST"

    name = request.form.get("name")
    text = request.form.get("text")

    name_len = len(name)
    text_len = len(text)

    if name_len > 100 or name_len == 0:
        return abort(400)
    if text_len > 3000 or text_len < 1:
        return abort(400)

    message = {
        "id": str(uuid.uuid4()),
        "name": name,
        "text": text,
        "time": time.time()
    }
    db.append(message)
    save_messages()

    return "OK"


def print_messages(messages):
    for message in messages:
        name = message["name"]
        text = message["text"]
        time = message["time"]
        time_pretty = datetime.datetime.fromtimestamp(time)
        print(f"[{name}] / {time_pretty}")
        print(text)


@app.route("/messages")
def get_messages():
    after_timestamp = float(request.args["after_timestamp"])
    result = []
    for message in db:
        if message["time"] > after_timestamp:
            result.append(message)

    return {"messages": result}


app.run()
