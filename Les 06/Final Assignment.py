def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print('Er zijn nog {} kluizen vrij.'.format(str(aantalvrij)))


def nieuwe_kluis():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for regel in kluizendata:
        gegevensvan1kluis = regel.split(';')
        stringkluisnummer = int(gegevensvan1kluis[0])
        print(stringkluisnummer)
        if stringkluisnummer in list:
            print('if')
            list.remove(stringkluisnummer)
            print(list)



#if len(list) > 0:
 #   outfile = open('')
  #  code = input('Voer uw code in: ')
   # if len(code) >=4:
    #    print('Uw kluisnummer is {}'.format(list[0]))
     #   infile.open('kluizen.txt', 'a')



#        else:
#            print('Uw code is niet geldig, voer een nieuwe code in.')



    if len(list) == 0:
        print('Er zijn helaas geen kluizen meer beschikbaar.')



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

