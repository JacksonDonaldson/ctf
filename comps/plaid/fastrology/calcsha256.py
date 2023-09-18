import hashlib

def shaSoln(startText):
    start = bytes(startText, "utf-8")

    i = 0
    while True:
        #print("?")
        s = str(i)
        s = s + "0" * (18 - len(start) - len(s))
        s = bytes(s, "utf-8")
        hashval = hashlib.sha256(start + s).hexdigest()
        val = str(hashval[-6:])
        if(val.count("f") > 5):
            return start + s
        #print(s)
        i+=1


