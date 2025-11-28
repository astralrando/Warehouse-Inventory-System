adding = {}
circulating = {}
addingTotes = True

while addingTotes:
    tote = input("Name your child: ")

    needs = input("Input Needs: ")

    adding[tote] = []
    adding[tote].append(needs)
    print(adding)
    print(adding.get(tote))