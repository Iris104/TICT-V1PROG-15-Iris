infile = open('Kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
print('Deze file telt {} regels'.format(len(regels)))

maximum = 0
regelnummer = 1
for regel in regels:
    kaartinfo = regel.split(',')
    nummer = int(kaartinfo[0])
    if nummer > maximum:
        maximum = nummer
        maxregelnummer = regelnummer
    regelnummer +=1
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(maximum, maxregelnummer))