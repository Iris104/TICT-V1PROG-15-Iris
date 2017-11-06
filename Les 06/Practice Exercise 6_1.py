def seizoen(maandnummer):
    if maandnummer == 3 or maandnummer == 4 or maandnummer == 5:
        print('Deze maand hoort bij de lente.')
    if maandnummer == 9 or  maandnummer == 10 or  maandnummer == 11:
        print('Deze maand hoort bij de herfst.')
    if maandnummer == 6 or  maandnummer == 7 or  maandnummer == 8:
        print('Deze maand hoort bij de zomer.')
    if maandnummer == 12 or  maandnummer == 1 or  maandnummer == 2:
        print('Deze maand hoort bij de winter.')

Januari = 1
Februari = 2
Maart = 3
April = 4
Mei = 5
Juni = 6
Juli = 7
Augustus = 8
September = 9
Oktober = 10
November = 11
December = 12
maandnummer = eval(input('Welke maand is het?'))

print(seizoen(maandnummer))
