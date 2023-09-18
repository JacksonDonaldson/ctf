#!/usr/local/bin/python
cod = input("sned cod: ")

if any(x not in "0[],.q(jw=_alsynxodtg)feum'zk:hivbcpr" for x in cod):
    print("bad cod")
else:
    try:
        print(eval(cod, {"__builtins__": {"dir":dir,"globals": globals, "locals": locals, "__import__": __import__}}))
    except Exception as e:
        print("oop", e)

#(a:=(__builtins__:=__import__('builtins'))==globals())
def test():
    global __builtins__
    __builtins__ = "fail"
    print(list("asdf"))
    print(locals())
    print(globals())
