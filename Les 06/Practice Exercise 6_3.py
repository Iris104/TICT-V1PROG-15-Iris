invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
lijst = invoer.split('-')
lijst = [int(i) for i in lijst]
lijst.sort()

groot = max(lijst)
klein = min(lijst)
aantal = len(lijst)
som = sum(lijst)
gem = som/aantal

print('Gesorteerde list van ints: {}'.format(lijst))
print('Grootste getal: {} en Kleinste getal: {}'.format(groot, klein))
print('Aantal getallen: {} en Som van de getallen: {}'.format(aantal, som))
print('Gemiddelde: {}'.format(gem))