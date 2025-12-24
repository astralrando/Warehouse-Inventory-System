import json

with open("data.json", "r") as zone:
    jsondata = zone.read()
    zones = json.loads(jsondata)