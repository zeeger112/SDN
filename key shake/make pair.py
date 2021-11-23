from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import math

#key generator
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("pub.pem", "wb")
file_out.write(public_key)
file_out.close()

# signing
with open("bericht.txt", 'rb') as bericht:
    bericht = bericht.read()
message = bericht
key = RSA.import_key(open('private.pem').read())
h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)
with open("berichthash.txt", 'wb') as hashpapier:
    hashpapier.write(signature)
