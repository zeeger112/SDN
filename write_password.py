import hashlib

wachtwoord = input("geef een wachtwoord op: ")

#hexidecimale hash van het wachtwoord wordt wegeschreven naar password.txt
whash = hashlib.sha256(wachtwoord.encode()).hexdigest()
with open("password.txt", "w") as hihi:
    hihi.write(whash)