def geefmelding(temperatuur):
    if temperatuur <= 0:
        print('Het vriest vandaag.')

    elif temperatuur >= 0 and temperatuur <= 15:
        print('Het is koud vandaag.')

    else:
        print('Het is lekker weer vandaag.')

temperatuur = eval(input('Welke temperatuur is het vandaag? '))
geefmelding(temperatuur)

