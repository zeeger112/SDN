import xml.etree.cElementTree as etree

tree = etree.parse ('./xml/netwerk.xml')
root = tree.getroot()

clients = root.findall('.//client')
for ding in clients:
    print("\nclient id:",ding.attrib['type'])
    print("os is:",ding.find('os').text)
    print("IP is:",ding.find('ip').text)

servers = root.findall('.//server')
for ding in servers:
    print("\nserver id:",ding.attrib['type'])
    print("os is:",ding.find('os').text)
    print("IP is:",ding.find('ip').text)