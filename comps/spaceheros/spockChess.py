from pwn import *

p = remote("spaceheroes-chess-with-spock.chals.io", 443, ssl=True, sni="spaceheroes-chess-with-spock.chals.io")


def printvals(value):
    
    
    v = value.split(b"\n")[1:-2]

    j = 8
    for line in v[:-1]:
        print(j, end = "")
        j-=1
        for i in range(9, len(line), 13):
            print(chr(line[i]), end = "")
        print()
    print(str(v[-1]))
##print("starting")
from time import sleep
sleep(.5)
while True:
    f = b"\n"
    nextPrint = False
    while f[-1] == 10:

        f = p.read()
        

        if(nextPrint):
            printvals(f)
        else:
            print(f)
        if f == b'##########':
            f = b'##########\n'
            nextPrint = True
        sleep(1)
    print("reading")
    i = bytes(input() + "\n", "utf-8")
    p.send(i)
    
