import hashlib

with open("password.txt", "r") as passwd:
    dsa = passwd.read()
wachtwoord = input("geef je wachtwoord op: ")
whash = hashlib.sha256(wachtwoord.encode()).hexdigest()
#vergelijkt de hash van jw wachtwoord met de opgeslagen hash
if whash == dsa:
    print("Wachtwoord OK")
else:
    print("Wachtwoord FOUT")