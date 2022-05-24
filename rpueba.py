from xml.dom import minidom

mydoc = minidom.parse('C:/Users/m.pirela.escobar/OneDrive - Accenture/Galicia/SMART/SMART_MDP_Contactos_V5.xml')


items = mydoc.getElementsByTagName('item')

# all item attributes
print('nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)