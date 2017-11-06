#File openen om te leze en toekennen aan een file object
infile = open('Kaartnummers.txt', 'r')
#File object inlezen m.b.v. readlines() en toekennen aan een list variabele
regels = infile.readlines()
#File sluiten
infile.close()
#(De list met strings afdrukken)
#print(regels)

#Herhaal voor elke regel
outfile = open('kaartnummersuit.tct', 'w')
for regel in regels:
    # De regel splitsen op de komma
    kaartinfo = regel.split(',')
    # I.p.v. print-opdracht:
    outfile.write('{} heeft kaartnummer: {}\n'.format(kaartinfo[1].strip(), kaartinfo[0]))
    # Let op: /n moet worden toegevoegd, omdat er anders verder wordt doorgeschreven op dezelfde regel!
#Als laatste regel toevoegen:
outfile.close()



