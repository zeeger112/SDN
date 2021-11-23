import hashlib
import string

p="326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"
Lijstmetletters = list(string.ascii_uppercase)
poging = 0
ww = list("123")
for letter in Lijstmetletters:
    ww[0] = letter
    for letter in Lijstmetletters:
        ww[1] = letter
        for letter in Lijstmetletters:
            ww[2] = letter
            wachtwoord = "".join(ww)
            if hashlib.sha224(wachtwoord.encode()).hexdigest() == p:
                print("Je hebt het wachtwoord gevonden! Het was:",ww)
                print("Met maar "+ str(poging)+' pogingen')
                exit
            else:
                poging += 1