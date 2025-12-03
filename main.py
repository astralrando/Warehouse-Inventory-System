#   Sorry, little weirdo. Threats won't work on me. 
#   I can't go to hell. I'm all out of vacation days :/

totesInz1A = []
totesInz2A = []
circulating = [{"name": "pt001", "items": ['33244']}]
addToZone = False
zones = ["z1a", "z2A"]

while True:

        # Enter main zones
        z1A = ['1A-101-A1', "1A-101-A2", '1A-101-A3', '1A-101-A4', '1A-101-A5', '1A-101-A6',
                '1A-101-B1', '1A-101-B2', '1A-101-B3', '1A-101-B4', '1A-101-B5', '1A-101-B6',
                '1A-101-C1', '1A-101-C2', '1A-101-C3', '1A-101-C4', '1A-101-C5', '1A-101-C6',
                '1A-101-D1', '1A-101-D2', '1A-101-D3', '1A-101-D4', '1A-101-D5', '1A-101-D6',
                '1A-101-E1', '1A-101-E2', '1A-101-E3', '1A-101-E4', '1A-101-E5', '1A-101-E6',

                '1A-102-A1', '1A-102-A2', '1A-102-A3', '1A-102-A4', '1A-102-A5', '1A-102-A6',
                '1A-102-B1', '1A-102-B2', '1A-102-B3', '1A-102-B4', '1A-102-B5', '1A-102-B6',
                '1A-102-C1', '1A-102-C2', '1A-102-C3', '1A-102-C4', '1A-102-C5', '1A-102-C6',
                '1A-102-D1', '1A-102-D2', '1A-102-D3', '1A-102-D4', '1A-102-D5', '1A-102-D6',
                '1A-102-E1', '1A-102-E2', '1A-102-E3', '1A-102-E4', '1A-102-E5', '1A-102-E6',

                '1A-103-A1', '1A-103-A2', '1A-103-A3', '1A-103-A4', '1A-103-A5', '1A-103-A6',
                '1A-103-B1', '1A-103-B2', '1A-103-B3', '1A-103-B4', '1A-103-B5', '1A-103-B6',
                '1A-103-C1', '1A-103-C2', '1A-103-C3', '1A-103-C4', '1A-103-C5', '1A-103-C6',
                '1A-103-D1', '1A-103-D2', '1A-103-D3', '1A-103-D4', '1A-103-D5', '1A-103-D6',
                '1A-103-E1', '1A-103-E2', '1A-103-E3', '1A-103-E4', '1A-103-E5', '1A-103-E6',

                '1A-104-A1', '1A-104-A2', '1A-104-A3', '1A-104-A4', '1A-104-A5', '1A-104-A6',
                '1A-104-B1', '1A-104-B2', '1A-104-B3', '1A-104-B4', '1A-104-B5', '1A-104-B6',
                '1A-104-C1', '1A-104-C2', '1A-104-C3', '1A-104-C4', '1A-104-C5', '1A-104-C6',
                '1A-104-D1', '1A-104-D2', '1A-104-D3', '1A-104-D4', '1A-104-D5', '1A-104-D6',
                '1A-104-E1', '1A-104-E2', '1A-104-E3', '1A-104-E4', '1A-104-E5', '1A-104-E6']

        z2A = ['2A-101-A1', '2A-101-A2', '2A-101-A3', '2A-101-A4', '2A-101-A5', '2A-101-A6',
                '2A-101-B1', '2A-101-B2', '2A-101-B3', '2A-101-B4', '2A-101-B5', '2A-101-B6',
                '2A-101-C1', '2A-101-C2', '2A-101-C3', '2A-101-C4', '2A-101-C5', '2A-101-C6',
                '2A-101-D1', '2A-101-D2', '2A-101-D3', '2A-101-D4', '2A-101-D5', '2A-101-D6',
                '2A-101-E1', '2A-101-E2', '2A-101-E3', '2A-101-E4', '2A-101-E5', '2A-101-E6',

                '2A-102-A1', '2A-102-A2', '2A-102-A3', '2A-102-A4', '2A-102-A5', '2A-102-A6',
                '2A-102-B1', '2A-102-B2', '2A-102-B3', '2A-102-B4', '2A-102-B5', '2A-102-B6',
                '2A-102-C1', '2A-102-C2', '2A-102-C3', '2A-102-C4', '2A-102-C5', '2A-102-C6',
                '2A-102-D1', '2A-102-D2', '2A-102-D3', '2A-102-D4', '2A-102-D5', '2A-102-D6',
                '2A-102-E1', '2A-102-E2', '2A-102-E3', '2A-102-E4', '2A-102-E5', '2A-102-E6',

                '2A-103-A1', '2A-103-A2', '2A-103-A3', '2A-103-A4', '2A-103-A5', '2A-103-A6',
                '2A-103-B1', '2A-103-B2', '2A-103-B3', '2A-103-B4', '2A-103-B5', '2A-103-B6',
                '2A-103-C1', '2A-103-C2', '2A-103-C3', '2A-103-C4', '2A-103-C5', '2A-103-C6',
                '2A-103-D1', '2A-103-D2', '2A-103-D3', '2A-103-D4', '2A-103-D5', '2A-103-D6',
                '2A-103-E1', '2A-103-E2', '2A-103-E3', '2A-103-E4', '2A-103-E5', '2A-103-E6',

                '2A-104-A1', '2A-104-A2', '2A-104-A3', '2A-104-A4', '2A-104-A5', '2A-104-A6',
                '2A-104-B1', '2A-104-B2', '2A-104-B3', '2A-104-B4', '2A-104-B5', '2A-104-B6',
                '2A-104-C1', '2A-104-C2', '2A-104-C3', '2A-104-C4', '2A-104-C5', '2A-104-C6',
                '2A-104-D1', '2A-104-D2', '2A-104-D3', '2A-104-D4', '2A-104-D5', '2A-104-D6',
                '2A-104-E1', '2A-104-E2', '2A-104-E3', '2A-104-E4', '2A-104-E5', '2A-104-E6']

        # Checks for circulating totes that need picks in the zone
        for tote in circulating:
                for item in tote['items']:
                        if item in z1A:
                                print("Item is in zone: 1A")
                                totesInz1A.append(circulating[0])
                                circulating.pop(0)
                                print(f'Totes in zone 1A: {totesInz1A}')
                                print(f'Totes circulating: {circulating}')
                                break
                        if item in z2A:
                                print("Item is in zone: 2A")
                                totesInz1A.append(circulating[0])
                                circulating.pop(0)
                                print(f'Totes in zone 1A: {totesInz2A}')
                                print(f'Totes circulating: {circulating}')
                                break

# MenuState System
        menus = ['0: Zone Checker', '1: Tote Induction', '2: Zone Scanner']
        for item in menus:
                print(item)
        menuState = int(input("Select a menu: "))

        if menuState == 1:
                print("Tote induction")

                toteName = input("Name tote: ")
                items = []

                while True:
                        item = input("Input SKU (leave blank to quit): ")
                        if item == "":
                                break
                        items.append(item)
                
                tote = {"name": toteName, "items": items}
                circulating.append(tote)

        if menuState == 0:
                print(f'Circulating line: {circulating}')
                print(f'In zone 1A: {totesInz1A}')
                print(f'in zone 2A: {totesInz2A}')
        
        if menuState == 2:
                enter_zone = input("Enter a zone: ")
                if enter_zone in zones:
                        
                        pass
                                