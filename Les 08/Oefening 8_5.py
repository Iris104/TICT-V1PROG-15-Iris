import random


def diceprob(invoersom):
    aantalworpinv = 0
    aantalworp = 0
    while aantalworpinv < 100:
        aantalogen1 = random.randrange(1, 7)
        aantalogen2 = random.randrange(1, 7)
        som = aantalogen1 + aantalogen2
        if som == invoersom:
            aantalworpinv += 1
        aantalworp += 1
    print('Het aantal benodigde worpen is {}'.format(aantalworp))


invoersom = eval(input('Hoe groot moet de som van twee ogen van een dobbelsteen zijn?'))
diceprob(invoersom)