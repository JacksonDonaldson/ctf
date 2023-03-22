l68 = "5e1b62514c5e495d"
l60 = "1f5819411b424249"
l58 = "5e75194e1b5f6d75"
l50 = "1e6d7519425e751a"
l48 = "1e750b0b53521e46"
l40 = "5718"

r = []
for s in [l68, l60, l58, l50, l48, l40]:
    v = []
    for i in range(0, len(s), 2):
        v.append(int(s[i:i+2], 16))

    r.extend(v[::-1])
        
def run(b):
    res = ""
    for i in range(len(r)):
        res += chr((r[i]) ^ b)
    print(res)

for i in range(257):
    run(i)
    
