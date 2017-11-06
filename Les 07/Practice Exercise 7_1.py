getal = eval(input('Geef een getal: '))
som = 0
while True:
    som = som + getal
    getal = eval(input('Geef een getal: '))
    if getal == 0:
        print('De som van de ingevoerde getallen is: {}'.format(som))
        break