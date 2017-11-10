def gemiddelde():
    zin = input('Geef een zin(4 woorden lang): ')
    zingesplit = zin.split(' ')
    woord1 = len(zingesplit[0])
    woord2 = len(zingesplit[1])
    woord3 = len(zingesplit[2])
    woord4 = len(zingesplit[3])
    lengte_zin = len(zingesplit)
    gemiddelde = (woord1 + woord2 + woord3 + woord4)/lengte_zin

    return gemiddelde


res = gemiddelde()
print(res)
