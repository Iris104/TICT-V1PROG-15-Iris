def swap (getallenlijst):
    if len(getallenlijst)>1:
        getallenlijst[0], getallenlijst[1] = getallenlijst [1], getallenlijst[0]
        return (getallenlijst)

getallenlijst = [4, 0, 1, -2]
res = swap (getallenlijst)
print(res)