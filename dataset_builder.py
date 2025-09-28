import json
data = []
while True:
    text = input("text >> ")
    if text == "stop":
        break
    # verse = input("verse >> ")
    text.replace("˺", "]")
    text.replace("˹", "[")
    data.append({
        "text":text,
        "label":"hope"
    })

with open("dataset.json", "a") as f:
    json.dump(data, f, indent=4)