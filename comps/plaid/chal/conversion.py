import sympy
from ast import literal_eval
string = "test string"

res = 'f\'{"".join(["0" * (8-len(bin(n)[2:])) + bin(n)[2:] for n in bytes(str(globals()), "utf-8")]).replace("0","a").replace("1","b")}\''
#print(res)
f = sympy.simplify(res)


r = res.replace("a", "0").replace("b", "1")
#print(r)


preeval=  "\"f\\\'{\\\"\\\".join([\\\"0\\\" * (8-len(bin(n)[2:])) + bin(n)[2:] for n in bytes(str(globals()), \\\"utf-8\\\")]).replace(\\\"0\\\",\\\"a\\\").replace(\\\"1\\\",\\\"b\\\")}\\\'\""
desiredstring = f'{"".join(["0" * (8-len(bin(n)[2:])) + bin(n)[2:] for n in bytes(str(globals()), "utf-8")]).replace("0","a").replace("1","b")}'

working = "\"f\\'{list(globals().keys())[0]}\\'\""

f = open("input.txt").read().replace("a", "0").replace("b", "1")
i = 0
while i < len(f):
    print(chr(int(f[i:i+8], 2)), end = "")
    i+=8
    
