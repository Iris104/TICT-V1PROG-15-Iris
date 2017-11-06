def inlezen_beginstation(stations):

    while True:
        beginstation = input('Welk station is uw beginstation? ')
        if beginstation in stations:
            return beginstation
            break
        else:
            print('Uw station bevindt zich niet in het traject Schagen-Maastricht.')

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Welk station is uw eindbestemming? ')
    while True:
        if eindstation in stations:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
                break
        else:
            print('Uw einbestemming bevindt zich niet in het traject Schagen-Maastricht.')
            eindstation = input('Welk station is uw eindbestemming? ')


def omroep_reis(stations, beginstation, eindstation):
    beginnummer = stations.index(beginstation) + 1
    eindnummer = stations.index(eindstation) + 1
    afstand = eindnummer - beginnummer
    prijs = afstand * 5
    tussenstations = []
    for i in range(stations.index(beginstation), stations.index(eindstation)):
        tussenstations.append(stations[i])


    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, beginnummer))
    print('Het eindstation {} is he {}e station in het traject.'.format(eindstation, eindnummer))
    print('De afstand bedraagt {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    print(' - {}'.format(tussenstations))
    print('Jij stapt uit in: {}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroep_reis(stations, beginstation, eindstation)
