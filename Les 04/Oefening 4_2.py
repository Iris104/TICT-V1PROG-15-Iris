def rng (getallenlijst):
    verschil = max(getallenlijst) - min(getallenlijst)
    return verschil

getallenlijst = [4, 0, 1, -2]
res = rng (getallenlijst)
print(res)