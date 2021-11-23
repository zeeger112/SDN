import xml.etree.cElementTree as etree

tree = etree.parse ('./xml/test.xml')
root = tree.getroot()
pointer = 0
lst1 = root.findall('.//S[@N="Message"]')
lst2 = root.findall('.//S[@N="MachineName"]')

for ding in root.findall('.//S[@N="Message"]'):
    deco = etree.tostring(lst1[pointer]).decode()
    deco2 = etree.tostring(lst2[pointer]).decode()
    print('error message: '+deco+'\n op machine'+deco2)
    pointer +=1