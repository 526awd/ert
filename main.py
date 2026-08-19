import requests as rt
import threading
f=open("a//a.txt","a+",encoding="utf8")
d=open("a//d.txt","a+",encoding="utf8")
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
def ty(p:int):
    for i in range(11000,1000000):
        e="http://cdn.sinacloud.net/edge.v.iask.com/%s.hlv"%i
        ad=rt.get(e,headers=headers)
        if ad.status_code==404:
            d.write(e+"\n")
        else:
            print(e+" pass")
            f.write(e+"\n")

f.close()
d.close()
