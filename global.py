print("I can't go to hell. I'm all out of vacation days :/")

#TODO
#Induction \/
#Tote eraser \/
#Picking
#Replenishment
#Zone entry
#Zone scanners
#Special pick inplementation
#Enter task

import json

# Initial variables
menustates = ["1: System Check", "2: Induction", "3: Tote eraser", "4: Pick Tote"]
menustate = 0

#   Parse JSON files
with open("data.json", "r") as zone:
    jsondata = zone.read()
    zones = json.loads(jsondata)

with open("totes.json", "r") as totes:
    totedata = totes.read()
    totes = json.loads(totedata)

print(totes)

while True:
    for item in menustates:
        print(item)
    menustate = int(input("Enter Menustate: "))

    # System Check
    if menustate == 1:

        print(zones)
        print(totes)
        menustate = 0

    # Induction
    if menustate == 2:
        needs = []
        toteName = input("Enter tote: ")
        while True:
            need = input("Input tote needs (leave blank to exit): ")
            if need == '':
                break
            needs.append(need)
        tote = {"name": toteName, "inTote": [], "needs": needs}
        totes.append(tote)
        print(totes)
        with open("totes.json", "w") as totedata:
            totepack = json.dumps(totes)
            totedata.write(totepack)
        menustate = 0
    
    # Tote Eraser
    if menustate == 3:
        erasetote = input("Input tote to remove: ")
        for tote in reversed(range(len(totes))):
            if totes[tote]['name'] == erasetote:
                del totes[tote]
        with open("totes.json", "w") as totedata:
            totepack = json.dumps(totes)
            totedata.write(totepack)
    
    # Picking
    if menustate == 4:
        pickzone = input("Enter Zone: ")
        for item in zones:
            if item['location'] == pickzone:
                print(item['location'])