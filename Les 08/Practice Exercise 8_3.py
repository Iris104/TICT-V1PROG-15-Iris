def code(invoerstring):
    asc = ord(invoerstring)
    for asc:
        asc += 3
        chr(asc)
    print(asc)

naam = str(input('Voer uw naam in: '))
beginstation = str(input('Voer uw beginstation in: '))
eindstation = str(input('Voer uw eindstation in: '))
invoerstring = str(naam+beginstation+eindstation)

res = code(invoerstring)
print(res)


