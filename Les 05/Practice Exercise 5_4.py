naam = input('Wat is je naam? ')
uur = input('Hoeveel uur heb je erover gedaan?')
min = input('Hoeveel minuten heb je erover gedaan?')
sec = input('Hoeveel seconden heb je erover gedaan?')

outfile = open('Hardlopers.txt', 'a')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
outfile.write('{}, {}:{}:{}, {}\n'.format(s, eval(uur), eval(min), sec, naam))
outfile.close()








