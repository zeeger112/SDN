import ftplib
import xml.etree.cElementTree as etree

tree = etree.parse ('./xml/FTP.xml')
root = tree.getroot()
conn = root.find('.//conn')

server = conn.find('server').text
username = conn.find('username').text
wachtwoord = conn.find('wachtwoord').text
target = conn.find('target').text
source = conn.find('source').text

print(server,username,wachtwoord,target,source)

ftp = ftplib.FTP(server,username,wachtwoord)
filename = source
with open(filename, "rb") as file:
    ftp.storbinary(f"STOR {target+filename}", file)