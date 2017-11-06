def vierletters():
    lijsttien = eval(input('Geef lijst met minimaal 10 strings: '))
    lijst = []

    for woord in lijsttien:
        len(woord) == 0
        if len(woord) == 4:
            lijst.append(woord)
        #if len(woord) == 4:
    #for woord in lijsttien
    return ('De nieuw-gemaakte lijst met alle vier-letter strings is: {}'.format(lijst))

print(vierletters())
