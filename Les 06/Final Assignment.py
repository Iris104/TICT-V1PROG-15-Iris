def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print('Er zijn nog {} kluizen vrij.'.format(str(aantalvrij)))


def nieuwe_kluis():
    nummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    for regel in kluizendata:
        regelsplitsen = regel.split(';')
        kluisnummer = int(regelsplitsen[0])
        if kluisnummer in nummers:
            nummers.remove(kluisnummer)

    if len(nummers) != 0:
        wachtwoord = input('Voer een wachtwoord in: ')
        if len(wachtwoord) < 4:
            print('Het wachtwoord moet minimaal 4 tekens lang zijn.')
        else:
            outfile = open('kluizen.txt', 'a')
            outfile.write('{};{}\n'.format(nummers[0], wachtwoord))
            print('Uw kluisnummer: {}'.format(nummers[0]))
            outfile.close()
    else:
        print('Alle kluizen zijn bezet.')
    infile.close()

def kluis_openen():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is je nummer?')
    code = input('Wat is je code?')
    gegevenscorrect = False
    for regel in kluizendata:
        gegevensvan1kluis = regel.split(';')
        stringkluisnummer = gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect:
        print('De gegevens zijn correct.')
    else:
        print('De gegevens zijn niet correct.')


print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
keuze = eval(input('Voer uw keuze in: '))

if keuze == 1:
    toon_aantal_kluizen_vrij()

elif keuze == 2:
    nieuwe_kluis()

else:
    kluis_openen()

