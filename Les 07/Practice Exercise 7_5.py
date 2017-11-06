namen = {'Valeria': 2, 'Bob': 2 , 'Amelie': 1}
naam = input('Volgende naam: ')

while True:
    if naam in namen:
        naam = input('Volgende naam: ')
    else:
        naam1 = 'Valeria'
        naam2 = 'Bob'
        naam3 = 'Amelie'
        nummer1 = 2
        nummer2 = 2
        nummer3 = 1
        print('Er is {} student met de naam {}'.format(nummer3, naam3))
        print('Er zijn {} studenten met de naam {}'.format(nummer2, naam2))
        print('Er zijn {} studenten met de naam {}'.format(nummer1, naam1))
        break
