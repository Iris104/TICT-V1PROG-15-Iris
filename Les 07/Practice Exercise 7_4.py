def ticker():
    dictionary = {}
    infile = open('ticker symbols.txt', 'r')
    regels = infile.readlines()
    infile.close()
    for regel in regels:
        regel = regel.strip().split(';')
        dictionary[regel[1]] = regel[0]
    return dictionary

def compleet(afkorting):
    if len(afkorting) < 4:
        afkorting = afkorting.upper()
        dict = ticker()
        return dict[afkorting]
    else:
        dict = ticker()
        for ticker1 in dict.values():
            if ticker1.lower() == afkorting:
                return ticker1

print(compleet(input('Waar wilt u het ticker symbol van weten? ')))



def ticker(filename):
    dictionary = {}
    keys = dictionary.keys()
    filename[0] = keys
    dictionary.append(keys)
    value = dictionary.values()
    filename[1] = value
    dictionary.append(value)
    return dictionary


infile = open('ticker symbols.txt', 'w')
filename = infile.readlines()
infile.close()
res = ticker(filename)
print(res)

