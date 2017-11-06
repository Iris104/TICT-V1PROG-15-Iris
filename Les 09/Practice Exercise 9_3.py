import csv
with open('Gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter = ';')
    hoogste_score = 0
    for row in reader:
        score = int(row[2])
        if score> hoogste_score:
            hoogste_score = score
            hoogste_naam = row[0]
            hoogste_datum = row[1]
    print('De hoogste score is: {} op {} behaald door {}.'.format(hoogste_score, hoogste_datum, hoogste_naam))

