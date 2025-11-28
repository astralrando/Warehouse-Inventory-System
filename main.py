#   Sorry, little weirdo. Threats won't work on me. 
#   I can't go to hell. I'm all out of vacation days :/

circulating = []
addToZone = False

while True:
        print(circulating)

        i101 = ['1A-101-A1', "1A-101-A2", '1A-101-A3', '1A-101-A4', '1A-101-A5', '1A-101-A6',
        '1A-101-B1', '1A-101-B2', '1A-101-B3', '1A-101-B4', '1A-101-B5', '1A-101-B6',
        '1A-101-C1', '1A-101-C2', '1A-101-C3', '1A-101-C4', '1A-101-C5', '1A-101-C6',
        '1A-101-D1', '1A-101-D2', '1A-101-D3', '1A-101-D4', '1A-101-D5', '1A-101-D6',
        '1A-101-E1', '1A-101-E2', '1A-101-E3', '1A-101-E4', '1A-101-E5', '1A-101-E6',]

        i102 = ['1A-102-A1', "1A-102-A2", '1A-102-A3', '1A-102-A4', '1A-102-A5', '1A-102-A6',
        '1A-102-B1', '1A-102-B2', '1A-102-B3', '1A-102-B4', '1A-102-B5', '1A-102-B6',
        '1A-102-C1', '1A-102-C2', '1A-102-C3', '1A-102-C4', '1A-102-C5', '1A-102-C6',
        '1A-102-D1', '1A-102-D2', '1A-102-D3', '1A-102-D4', '1A-102-D5', '1A-102-D6',
        '1A-102-E1', '1A-102-E2', '1A-102-E3', '1A-102-E4', '1A-102-E5', '1A-102-E6']
 
        i103 = ['1A-103-A1', "1A-103-A2", '1A-103-A3', '1A-103-A4', '1A-103-A5', '1A-103-A6',
        '1A-103-B1', '1A-103-B2', '1A-103-B3', '1A-103-B4', '1A-103-B5', '1A-103-B6',
        '1A-103-C1', '1A-103-C2', '1A-103-C3', '1A-103-C4', '1A-103-C5', '1A-103-C6',
        '1A-103-D1', '1A-103-D2', '1A-103-D3', '1A-103-D4', '1A-103-D5', '1A-103-D6',
        '1A-103-E1', '1A-103-E2', '1A-103-E3', '1A-103-E4', '1A-103-E5', '1A-103-E6']

        i104 = ['1A-104-A1', "1A-104-A2", '1A-104-A3', '1A-104-A4', '1A-104-A5', '1A-104-A6',
        '1A-104-B1', '1A-104-B2', '1A-104-B3', '1A-104-B4', '1A-104-B5', '1A-104-B6',
        '1A-104-C1', '1A-104-C2', '1A-104-C3', '1A-104-C4', '1A-104-C5', '1A-104-C6',
        '1A-104-D1', '1A-104-D2', '1A-104-D3', '1A-104-D4', '1A-104-D5', '1A-104-D6',
        '1A-104-E1', '1A-104-E2', '1A-104-E3', '1A-104-E4', '1A-104-E5', '1A-104-E6']

        z1A = [i101, i102, i103, i104]

        totesInz1A = []

        if len(circulating) > 0:
               print(circulating[0])

        for need in circulating:
            for item in z1A:
                if need in item:
                        print('added')
                        addToZone = True

        if addToZone == True:
                pass


# MenuState System

        addingTotes = False
        adding = {}

        menuState = int(input("Select a menu: "))

        if menuState == 1:
                print("Tote induction")
                addingTotes = True
        while addingTotes:
                tote = input("Tote name: ")
                if tote == "end":
                        break
                adding[tote] = input("Input need SIN: ")
                circulating.append(adding)
                adding = {}
                print(f'Circulating: {circulating}')