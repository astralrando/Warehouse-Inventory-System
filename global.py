import json

# Initial variables
menustates = ["1: System Check", "2: Induction"]
menustate = 0

# Get data from JSON files
with open("data.json", "r") as zone:
    jsondata = zone.read()
    data = json.loads(jsondata)

with open("totes.json", "r") as totes:
    totedata = totes.read()
    totes = json.loads(totedata)

for item in menustates:
    print(item)
menustate = int(input("Enter Menustate: "))

if menustate == 1:

    print("Totes: ")
    for item in totes:
        print(item)
    print("Zones: ")
    for item in data:
        print(item)

# Induction
if menustate == 2:
    needs = []
    toteName = input("Enter tote: ")
    while True:
        need = input("Input tote needs (leave blank to exit): ")
        if need == "":
            break
        needs.append(need)
    tote = {"name": toteName, "inTote": [], "needs": needs}
