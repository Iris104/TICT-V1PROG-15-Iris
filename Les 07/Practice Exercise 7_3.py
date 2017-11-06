cijfers = {'Iris': 9, 'Lars': 7, 'Maartje': 8, 'Kees': 10, 'Peter': 9, 'Yvonne': 8, 'Ellen': 10, 'Thomas': 6}
for student in cijfers:
    if cijfers[student] >= 9:
        print('{} heeft een {}'.format(student, cijfers[student]))