def eindbedrag(bedrag, rente):
    bedrag = (bedrag + (bedrag * (rente/100)))
    return(bedrag)

bedrag = eval(input('Wat is uw bedrag?'))
rente = eval(input('Wat is uw rentepercentage? '))
res = eindbedrag(bedrag, rente)
print(res)
