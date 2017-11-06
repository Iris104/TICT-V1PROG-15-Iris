def berekensomevengetallen(getallenrij):
    som = 0
    for getal in getallenrij:
        if getal % 2 == 0:
            som = som + getal
    return som

def berekensomonevengetallen(getallenrij):
    som = 0
    for getal in getallenrij:
        if getal % 2 > 0:
            som = som + getal
    return som

getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
res = berekensomevengetallen(getallenrij)
res1 = berekensomonevengetallen(getallenrij)
print('De som van de even getallen bedraagt {}'.format(res))
print('De som van de oneven getallen bedraagt {}'.format(res1))
