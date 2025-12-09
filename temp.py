import json

menustate = 0

menustate = int(input("Enter menustate: "))

with open("data.json", "r") as file:
    data = file.read()
    print(data)

if menustate == 1:
    with open("data.json", "w") as file:

        data = json.loads(data)

        something = ["something", "other thing"]

        thing = ["oops i killed it"]

        for item in something:
            thing.append(item)
        
        data = data + thing

        thing = json.dumps(thing)
        file.write(thing)

    print(thing)