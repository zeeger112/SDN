from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

with open("berichthash.txt", "rb") as papierhash:
    signature = papierhash.read()
with open("bericht.txt", 'rb') as bericht:
    bericht = bericht.read()
message = bericht
key = RSA.import_key(open('pub.pem').read())
h = SHA256.new(message)
try:
    pkcs1_15.new(key).verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")
