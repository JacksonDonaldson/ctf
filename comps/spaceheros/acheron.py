from pwn import *
p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
#p.interactive()
print("done")
p.send(b"NENWSSEWSNENSSWEENWSNNESS")
print(p.read())
print(p.read())
print(p.read())
import time
time.sleep(1)
print(p.read())
print(p.readall())
