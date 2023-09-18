#!/usr/bin/env python3

from random import randint

a = randint(0, 2**32 - 1) | 1
b = randint(0, 2**32 - 1) | 1
c = randint(0, 2**32 - 1) | 1
x = randint(0, 2**32 - 1) | 1

b = 1823866125
a = 3848410295
c = 3275044927
x = 591196841
 
def get_next():
    global a, b, c, x
    x = (a*x**2 + b*x + c) % 2**32
    return x

#flag = open("flag.txt", "rb").read()
flag = b'\x12>\xd3gx\xb1\xbdx?#\x99\xdf\x0ck:\xf1o\xe2\xb3\x88\xceP\xb0\xb0\xcc\x01\xbb\x8e\x86\x16\x1a6\xfaQ\xab\x9e7\xfdj\x86\xe9\xa4\x83\xc2\xb2\xb8'

ct = bytes((get_next()^c)%256 for c in flag)
print(ct)

# Output:
f = b'\x12>\xd3gx\xb1\xbdx?#\x99\xdf\x0ck:\xf1o\xe2\xb3\x88\xceP\xb0\xb0\xcc\x01\xbb\x8e\x86\x16\x1a6\xfaQ\xab\x9e7\xfdj\x86\xe9\xa4\x83\xc2\xb2\xb8'

from z3 import *

a = BitVec("a", 32)
b = BitVec("b", 32)
c = BitVec("c", 32)
x = BitVec("x", 32)

conditions = []
for val in [a,b,c,x]:
    conditions.extend([val | 1 == val])
    
x2 = (a * x * x + b * x + c)
conditions.append((x2^BitVecVal(ord("i"), 32) % 256)== BitVecVal(f[0], 32))

x3 = (a * x2 * x2 + b * x2 + c)
conditions.append((x3^BitVecVal(ord("c"), 32) % 256)== BitVecVal(f[1], 32))

x4 = (a * x3 * x3 + b * x3 + c)
conditions.append((x4^BitVecVal(ord("t"), 32) % 256)== BitVecVal(f[2], 32))

x5 = (a * x4 * x4 + b * x4 + c)
conditions.append((x5^BitVecVal(ord("f"), 32) % 256)== BitVecVal(f[3], 32))
solve(conditions)
