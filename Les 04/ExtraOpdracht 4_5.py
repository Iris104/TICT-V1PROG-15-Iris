def berekensomevengetallen(getallenrij):
    som = 0
    for getal in getallenrij:
        if getal % 2 == 0:
            som = som + getal
    print('De som van de even getallen bedraagt {}'.format(som))

getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
berekensomevengetallen(getallenrij)