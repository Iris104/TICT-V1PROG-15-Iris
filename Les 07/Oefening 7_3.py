#De zin declareren
zin = 'all animals are equal but some animals are more equal than other'

#De zin splitsen op de spatie (je krijgt dan een list met strings)
woorden = zin.split()

#Initialiseer woordenlijst op lege dictionary
woordenteller = {}

#Doorloop de list (als het woord voorkomt, teller met 1 ophogen. Anders woord toevoegen aan dictionary en teller op 1 zetten.)
for woord in woorden:
    if woord in woordenteller.keys():
        woordenteller[woord] += 1
    else:
        woordenteller[woord] = 1
    # Fatsoeneren output
    print('{:8} komt {:1} keer voor.'.format(woord, woordenteller[woord]))

