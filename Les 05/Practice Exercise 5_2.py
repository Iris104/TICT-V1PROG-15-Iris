#File openen om te leze en toekennen aan een file object
infile = open('Kaartnummers.txt', 'r')
#File object inlezen m.b.v. readlines() en toekennen aan een list variabele
regels = infile.readlines()
#File sluiten
infile.close()
#(De list met strings afdrukken)
#print(regels)

#Herhaal voor elke regel
for regel in regels:
    # De regel splitsen op de komma
    kaartinfo = regel.split(',')
    # regel afdrukken
    print('{} heeft een kaartnummer: {}'.format(kaartinfo[1].strip(), kaartinfo[0]))

