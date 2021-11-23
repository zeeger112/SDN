import random
import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT

teller = 0
rannum = list()
for niks in range(1000):
    num = random.randrange(500)
    rannum.append(num)
conn = sqlite3.connect("numdb.db")
c=conn.cursor()
c.execute ("CREATE TABLE nummers ('getal' INTEGER)")
for ding in rannum:
     query = "INSERT into nummers VALUES (" + str(ding) +");"
     c.execute(query)
conn.commit()
c.execute ("SELECT avg(getal) FROM nummers ")
print("wat is dit:",c.fetchall())
c.execute ("SELECT min(getal) FROM nummers ")
print("wat is dit:",c.fetchall())
c.execute ("SELECT max(getal) FROM nummers ")
print("wat is dit:",c.fetchall())
conn.close()
