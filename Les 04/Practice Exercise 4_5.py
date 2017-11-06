def kwadraten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal >= 0:
            som = som + getal**2
    return som


grondgetallen = [4, 5, 3, -81]
res = kwadraten_som(grondgetallen)
print(res)