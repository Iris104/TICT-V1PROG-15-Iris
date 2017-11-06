bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print(groen.intersection(bruin))
print(bruin.difference(groen))
print(bruin.union(groen))