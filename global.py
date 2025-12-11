import json

# Get data from JSON files
with open("data.json", "r") as zone:
    jsondata = zone.read()
    data = json.loads(jsondata)

with open("totes.json", "r") as totes:
    totedata = totes.read()
    totes = json.loads(totedata)

for item in totes:
    print(item)
