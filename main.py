import requests as rt
import threading
import time
f=open("a//a.txt","a+",encoding="utf8")
d=open("a//d.txt","a+",encoding="utf8")
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
def ty(p:int,o:int):
    for p in range(p,o):
        e="http://cdn.sinacloud.net/edge.v.iask.com/%s.hlv"%p
        time.sleep(0.00001)
        try:
            ad=rt.get(e,headers=headers)
        except Exception:
            try:
                ad=rt.get(e,headers=headers)
            except Exception:
                print(e+" unknow")
        if ad.status_code==404:
            d.write(e+"\n")
        else:
            print(e+" pass")
            f.write(e+"\n")
l=0
kt=[]
for i in range(10000,10000000,5000):
    t = threading.Thread(target=ty, args=(l,i))
    l=i
    kt.append(t)
    print(i)
for kl in kt:
    kl.start()
for kl in kt:
    kl.join()

f.close()
d.close()
