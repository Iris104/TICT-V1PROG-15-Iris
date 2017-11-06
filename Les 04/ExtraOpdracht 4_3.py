def eindbedrag(bedrag, rente):
    bedrag = (bedrag + (bedrag * (rente/100)))
    print(bedrag)

bedrag = eval(input('Wat is uw bedrag?'))
rente = eval(input('Wat is uw rentepercentage? '))
eindbedrag(bedrag, rente)