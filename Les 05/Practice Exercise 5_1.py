def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def table():
    print('    F     C')
    for tempG in range (-30, 41, 10):
        fahrenheit = convert(tempG)
        print('{:6.1f} {:6.1f}'.format(fahrenheit, tempG))

table()