import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse((filestring))
        return xmldictionary

stationsdict = processXML('FA.xml')
stations = stationsdict['Stations']['Station']


print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    code = station['Code']
    type = station['Type']
    print('{:4} - {}'.format(code, type))

print('Dit zijn alle stations op één of meer synoniemen: ')
for station in stations:
    code = station['Code']
    synoniemen = station['Synoniemen']
    if synoniemen is not None:
        print('{:4} - {}'.format(code, synoniemen))

print('Dit is de lange naam van elk station: ')
for station in stations:
    code = station['Code']
    lange_naam = station['Namen']['Lang']
    print('{:4} - {}'.format(code, lange_naam))