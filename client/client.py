import sys
import requests

api_url = "http://127.0.0.1:8008"

action = sys.argv[1]
if action == "send":
    username = sys.argv[2]
    message = sys.argv[3]
    try:
        with open("self_message_counter") as f:
            self_message_count = str(int(f.read()) + 1)
    except FileNotFoundError:
        self_message_count = "1"
    requests.post(f"{api_url}/modify", json={
        "key": f"messages/{username}-{self_message_count}",
        "value": f"{username}: {message}",
    })
    with open("self_message_counter", "w") as f:
        f.write(self_message_count)
    print("sent")
elif action == "poll":
    successful_polls = 0
    while True:
        try:
            with open("last_layer_number") as f:
                query_layer_number = str(int(f.read()) + 1)
        except FileNotFoundError:
            query_layer_number = "1"
        response = requests.post(f"{api_url}/get_layer", json={
            "layer_number": query_layer_number,
        }).json()
        if response is None:
            break
        else:
            value = response["value"]
            if response["key"].startswith("messages/") and value is not None:
                with open("chat.txt", "a", encoding="utf-8") as f:
                    f.write(value + "\n")
            with open("last_layer_number", "w") as f:
                f.write(query_layer_number)
            successful_polls += 1
    print(f"received: {successful_polls}")
else:
    raise Exception("Unknown action")
