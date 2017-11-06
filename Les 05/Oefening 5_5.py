#A)
#File openen om te lezen en toekennen aan een file object
infile = open('Voorbeeld 5_5.txt', 'r')
#File object inlezen m.b.v. read() en toekennen aan een stringvariabele
inhoud = infile.read()
#File sluiten
infile.close()
#String afdrukken
print(inhoud)

#B)
#File openen om te lezen en toekennen aan een file object
infile = open('Voorbeeld 5_5.txt', 'r')
#File object inlezen m.b.v. read() en toekennen aan een stringvariabele
inhoud1 = infile.read()
#File sluiten
infile.close()
#Van de string een lijst van strings maken gesplitst op de spatie en toekennen aan een nieuwe variabele
inhoud2 = inhoud.split()
#Lijst van strings afdrukken
print(inhoud2)

#C)
#File openen om te lezen en toekennen aan een file object
infile = open('Voorbeeld 5_5.txt', 'r')
#File object inlezen m.b.v. readlines en toekennen aan een listvariabele
inhoud3 = infile.readlines()
#File sluiten
infile.close()
#De list met stings afdrukken
print(inhoud3)