#De gebuiker een zin laten invoeren
zin = input('Voer een zin in: ')
#Spilts de zin op de spatie en ken deze toe aan een list variabele
woorden = zin.split()
#Begin met een leeg acronym
acroniem = ''
#Doorloop de woorden van de list. Voeg eerst de letter van het woord als hoofdletter toe aan acroniem
for woord in woorden:
    acroniem = acroniem + woord[0].upper()
#Druk acroniem af
print(acroniem)