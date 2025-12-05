#   I can't go to hell. I'm all out of vacation days :/

totesIni1 = []
totesIni2 = []
circulating = [{"name": "pt001", "items": ['i1-e3']}]
addToZone = False
zones = ["z1a", "z2A"]
menuState = 0

while True:

        # Zones Init
        i1 = [ 'i1-a1', 'i1-a2', 'i1-a3', 'i1-a4', 'i1-a5', 'i1-a6',
                'i1-b1', 'i1-b2', 'i1-b3', 'i1-b4', 'i1-b5', 'i1-b6',
                'i1-c1', 'i1-c2', 'i1-c3', 'i1-c4', 'i1-c5', 'i1-c6',
                'i1-d1', 'i1-d2', 'i1-d3', 'i1-d4', 'i1-d5', 'i1-d6',
                'i1-e1', 'i1-e2', 'i1-e3', 'i1-e4', 'i1-e5', 'i1-e6',]

        i2 = [ 'i2-a1', 'i2-a2', 'i2-a3', 'i2-a4', 'i2-a5', 'i2-a6',
                'i2-b1', 'i2-b2', 'i2-b3', 'i2-b4', 'i2-b5', 'i2-b6',
                'i2-c1', 'i2-c2', 'i2-c3', 'i2-c4', 'i2-c5', 'i2-c6',
                'i2-d1', 'i2-d2', 'i2-d3', 'i2-d4', 'i2-d5', 'i2-d6',
                'i2-e1', 'i2-e2', 'i2-e3', 'i2-e4', 'i2-e5', 'i2-e6',]

        isp = [ 'isp-a1', 'isp-a2', 'isp-a3', 'isp-a4', 'isp-a5', 'isp-a6',
                'isp-b1', 'isp-b2', 'isp-b3', 'isp-b4', 'isp-b5', 'isp-b6',
                'isp-c1', 'isp-c2', 'isp-c3', 'isp-c4', 'isp-c5', 'isp-c6',
                'isp-d1', 'isp-d2', 'isp-d3', 'isp-d4', 'isp-d5', 'isp-d6',
                'isp-e1', 'isp-e2', 'isp-e3', 'isp-e4', 'isp-e5', 'isp-e6',]

        # Checks for circulating totes that need picks in zones
        if menuState == 11:
                for tote in circulating:
                        for item in tote['items']:
                                if item in i1:
                                        print("Item is in zone: i1")
                                        totesIni1.append(circulating[0])
                                        totesIni1.pop(0)
                                        print(f'Totes in zone i1: {totesIni1}')
                                        print(f'Totes circulating: {circulating}')
                                        break
                                if item in i2:
                                        print("Item is in zone: i2")
                                        totesIni2.append(circulating[0])
                                        totesIni1.pop(0)
                                        print(f'Totes in zone i2: {totesIni2}')
                                        print(f'Totes circulating: {circulating}')
                                        break

# MenuState System
        menus = ['0: Zone Checker', '1: Tote Induction', '2: Zone Scanner (i1)',
                 '3: SKU Picking', '11: Auto Zone Entry']
        print('')
        for item in menus:
                print(item)
        menuState = int(input("Select a menu: "))

        if menuState == 0:
                print("")
                print(f'Circulating line: {circulating}')
                print(f'In zone i1: {totesIni1}')
                print(f'in zone i2: {totesIni2}')

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

        
        if menuState == 2:
                enter_tote = input("Enter a tote: ")
                for item in tote['items']:
                        if item in i1:
                                i1.append(enter_tote)
                                circulating.pop(tote)
        
        if menuState == 3:
                on_cart = []
                zone = input("Zone ID: ")
                cart = input("Cart ID: ")
                if zone in zones:
                        print(True)
                while True:
                        pick_tote = input("Enter Tote: ")
                        if pick_tote == "":
                                break
                on_cart.append(pick_tote)