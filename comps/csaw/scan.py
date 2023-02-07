import requests
from selenium import webdriver

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }

currentLink = "/stuff"
pre = "http://web.chal.csaw.io:5010"
total = currentLink
d = webdriver.Firefox()

while True:
    d.get(pre + currentLink)
    
    rtext = d.page_source
    v = rtext.index("href") + 1
    i = v + rtext[v:].index("href")
    lStart = rtext[i:].index('"') + i
    lEnd = rtext[lStart + 1:].index('"')
    s = rtext[lStart+1:lEnd+lStart+1]
    total += currentLink
    currentLink = s
    print(s)
