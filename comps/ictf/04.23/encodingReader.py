f = open("encoded.txt", "rb")
t = f.read()
a = t.replace(b"0", b"a")
a = a.replace(b"1", B"a")
b = a.replace(b"\r\n", b"1").replace(b"\n", b"0")
c = [i for i in b if i == 49 or i == 48]

d = "".join([chr(i) for i in c])

print(d)
