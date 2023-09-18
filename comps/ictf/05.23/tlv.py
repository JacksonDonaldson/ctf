import string

encoded = [1, 4, 8, 2, 19, 5, 4, 1, 123, 2, 1, 2, 1, 2, 20, 18, 2, 1, 19, 1, 2, 14, 12, 4, 1, 95, 1, 1, 19, 2, 1, 24, 1, 2, 15, 4, 4, 1, 95, 1, 6, 11, 4, 13, 6, 19, 7, 4, 1, 95, 1, 5, 21, 0, 11, 20, 4, 4, 1, 95, 2, 5, 19, 24, 15, 4, 18, 4, 1, 95, 3, 3, 1, 4, 1, 1, 2, 0, 1, 4, 1, 125]

next = False
opcode = None
running = 0

def printType(code, value):
    if code == 1:
        print(string.ascii_lowercase[value], end = "")
    elif code == 2:
        print(string.ascii_uppercase[value], end = "")
    elif code == 3:
        print(value, end = "")
    elif code == 4:
        print(chr(value), end = "")
    else:
        print("?", code , end = "")


for e in encoded:
    if next:
        running = e
        next = False
    elif running > 0:
        printType(opcode, e)
        running-=1
    else:
        opcode = e
        next = True
