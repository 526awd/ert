import requests as rt
import time
w=rt.get("https://uapis.cn/api/v1/misc/weather",params = {"city":"weifang","forecast":True,"lang":"zh"})
print(w.text)
wemsg_j=w.json()
wemsg="今天天气\n"+wemsg_j["province"]+"  "+wemsg_j["city"]+"\n气温 "+"最高"+str(wemsg_j["temp_max"])+"°C 最低"+str(wemsg_j["temp_min"])+"°C 当前"+str(wemsg_j["temperature"])+"°C 天气"+" "+wemsg_j["weather"]+"\n"+wemsg_j["wind_power"]+wemsg_j["wind_direction"]+"\n"+ wemsg_j["report_time"]
p=rt.get("https://uapis.cn/api/v1/saying/random",params = {"mode":"daily"})
pa=p.json()["item"]["content"]
pm=p.json()["item"]["author"]
pl=pa+"\n"+"          "+pm
print(wemsg)
params={"apikey":"ZJYOMP6JSEY3THLYO6MA2Y26","from":1132345,"body":wemsg}
url="https://api.nekoko.tel/sms/send/37254116083"
q=rt.get(url,params=params)
time.sleep(5)
params={"apikey":"ZJYOMP6JSEY3THLYO6MA2Y26","from":1132340,"body":"一言\n"+pl}
p=rt.get(url,params=params)
