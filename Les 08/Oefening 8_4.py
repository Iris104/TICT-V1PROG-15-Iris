woord = input('Voer een woord in: ')

#Herhaal voor iedere karakter uit de string
#Bereken ascii-waarde van het karakter
for letter in woord:
    code = ord(letter)
    #Druk achter elkaar af het karakter, de ascii-waarde van het karakter, de hexadecimale notatie en de binaire code
    print('{} {} {:x} {:b}'.format(letter, code, code, code))

