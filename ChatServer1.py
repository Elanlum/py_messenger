import time
import datetime

message = {
    "text": "Hello, Ivan",
    "name": "Donald", 
    "time": time.time()
}

db = [
    message
]



def chat( name, text):
    message = {
        "text": text,
        "name": name, 
        "time": time.time()
    }

    db.append(message)

def print_messages(messages):
    for message in messages:
        name = message["name"]
        text = message["text"]
        time = message["time"]
        time_pretty = datetime.datetime.fromtimestamp(time)
        print(f"[{name}] / {time_pretty}")
        print(text)

print_messages(db)
