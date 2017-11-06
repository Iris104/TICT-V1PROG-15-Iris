#Deel 1
def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = 15 + afstandKM * 0.60
        return(prijs)
    if afstandKM < 0:
        prijs = 0
        return(prijs)
    else:
        prijs = afstandKM * 0.80
        return(prijs)


# Deel 2
def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        prijsrit = 0.70 * standaard
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        prijsrit = 0.65 * standaard
    if leeftijd > 12 or leeftijd < 65 and weekendrit == False:
        prijsrit = standaard
    if leeftijd > 12 or leeftijd < 65 and weekendrit == True:
        prijsrit = 0.60 * standaard
    return prijsrit

leeftijd = eval(input('Wat is uw leeftijd? '))
weekendrit = input('Reist u in het weekend? (ja of nee) ')
if weekendrit == 'ja' or weekendrit == 'Ja':
    weekendrit == True
if weekendrit == 'nee' or weekendrit == 'Nee':
    weekendrit == False
afstandKM = eval(input('Hoeveel kilometer heeft u gereisd? '))

res = ritprijs(leeftijd, weekendrit, afstandKM)
print('Uw ticket zal ' + str(res) + ' euro kosten.')




