import json
import main

with open("data.json", "r") as file:
    data = file.read()
    jsondata = json.loads(data)

print(jsondata)

run = False
if run == True:
    jsondata[0]['quantity']-=1
    with open("data.json", "w") as file:
        packfile = json.dumps(jsondata)
        file.write(packfile)
    print(packfile)

def replenish(count):
    with open("data.json", "w") as file:
        toreplenish = jsondata[main.location]["quantity"]