import socket
import sys
import subprocess
from subprocess import call
import time
import datetime

HOST = '' # Alle beschikbare interfaces
try:
    PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)
except Exception:
    print(Exception)
    exit

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except Exception:
    print(Exception)
    exit
try:
    s.listen(10)
except Exception:
    print(Exception)
    exit
print('> Socket luistert op poort:',PORT)
# Wacht op connecties (blocking)
conn, addr = s.accept()
# Er is een client verbonden met de server
print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
# De server meldt zich aan de client
conn.sendall(b'WelkomOpMijnServer, vertel me iets, dan zeg ik hetzelfde terug: ')
# Wacht op input van de client en geef deze ook weer terug (echo service)
loop = True
while loop == True:
    data = conn.recv(1024)
    #lees overige data omdat putty niet goed werkt
    conn.recv(5000)
    data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
    print('> Client data ontvangen:'+data+'<eindeData>')
    conn.sendall(b"jeStuurdeMijDezeData:"+data.encode())
    conn.sendall(b'\r\n:')
    # Verbreek de verbinding en sluit de socket
    if data == "stop":
        conn.r
        s.close()
        loop = False
    if data == "CALC" or data == "NOTEPAD":
        conn.sendall(b'Wat is het wachtwoord?: ')
        wdata = conn.recv(1024)
        #lees overige data omdat putty niet goed werkt
        conn.recv(5000)
        #wdata=str(wdata.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
        tt =time.time()
        time2 = datetime.datetime.fromtimestamp(tt).strftime('%Y%m%d_%H:%M:%S - ')
        if wdata == b"hi" and data == 'CALC':
            call(["calc.exe"])
            with open("log.txt", "a") as log:
                log.write(time2 + "Calculator is geopend")
        elif wdata == b"hi":
            call(["notepad.exe"])
            with open("log.txt", "a") as log:
                log.write(time2 + "Notepad is geopend")



        



