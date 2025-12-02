totes = []
circulating = []


name = input("Name tote: ")
items = []

while True:
    item = input("Add item (blank to stop): ")
    if item == "":
        break
    items.append(item)

tote = {"name": name, "items": items}
totes.append(tote)

print(totes)