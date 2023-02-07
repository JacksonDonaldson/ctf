import re

from Crypto.Hash import SHA256  # md5 is broken! let's use a better hash.

LAT = '42'
LON = '-83'

def geohash(date, key):
  h = SHA256.new()
  h.update(date + key)
  lat = h.hexdigest()[0:32]
  lon = h.hexdigest()[32:64]

  lat = re.sub(r'[a-f]', '', lat)
  lon = re.sub(r'[a-f]', '', lon)
  return LAT + '.' + lat, LON + '.' + lon

s = "abcdefghijklmnopqrstuvwxyz"

from itertools import product

j = 0
for i in list(product(s, repeat = 4)):
    j+=1
    if j % 10000 == 0:
        print(j)
    key = bytes("".join(i), "utf-8")
    #print(key)
    if geohash(b'2022-10-23', key) == ('42.58315648926427644928', '-83.797263344109028598897145'):
        print(1, i)
        if(geohash(b'2022-10-24', key) == ('42.040627386680425592', '-83.762355007935356072702')):
           if geohash(b'2022-10-25', key) == ('42.26923766295854915', '-83.1128011532624330972'):
               print(i)
