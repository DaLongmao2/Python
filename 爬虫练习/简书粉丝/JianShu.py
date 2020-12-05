# coding = utf-8
import lxml.html
import requests
import re
import pandas as pd


import requests
url = "https://mp.weixin.qq.com/mp/profile_ext"
querystring = {"action":"getmsg","__biz":"MzA4NzA1OTc5Nw==","f":"json","offset":"20","count":"10","appmsg_token":"936_iWFH%2F9haOTPb6GApBj6wXjPGKg9eeU7slzmH2Q~~"}
headers = {
    'user-agent': "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    'accept-encoding': "gzip, deflate",
    'accept': "*/*",
    'connection': "keep-alive",
    'host': "mp.weixin.qq.com",
    'x-requested-with': "XMLHttpRequest",
    'referer': "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA4NzA1OTc5Nw==&scene=124&devicetype=android-25&version=26051732&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=lLCqBwwrZ581bGDqrEkRsgjKkWYNPdUBs9grSaFjd79hSX0mdvR8%%2BLUbHoWGGBEp&wx_header=1",
    'accept-language': "zh-CN,en-US;q=0.8",
    'cookie': "pgv_pvi=4831552512; pgv_si=s989715456; sd_userid=18991505459750403; sd_cookie_crttime=1505459750403; tvfe_boss_uuid=a8e4e4f1ab6cd93d; pgv_info=ssid=s8735681072; pgv_pvid=4201362299; rewardsn=8d8b49dfb1811092eefe; wxtokenkey=19643e9f2ee569a10857d365bba88556d220fd33c1a0666b5d028a72b5bcd901; wxuin=838107840; devicetype=android-25; version=26051732; lang=zh_CN; pass_ticket=lLCqBwwrZ581bGDqrEkRsgjKkWYNPdUBs9grSaFjd79hSX0mdvR8+LUbHoWGGBEp; wap_sid2=CMCF0o8DElxUVDVJR3o1ZldpbDlHWWdjQ0xMU3lxM3BWTUozTFFuZFhrUEJaanhoSmZ1aEVncnU0VzFIaWR3QkVVVXFuTUlMTlkxNFZjTnRCMEt1VHJjV3UzQVNOYWdEQUFBfjD6rvjRBTgMQJRO",
    'q-ua2': "QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.23&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MI6 &RL=1080*1920&OS=7.1.1&API=25",
    'q-guid': "569ade09b5931656e4f49098113e88cb",
    'q-auth': "31045b957cf33acf31e40be2f3e71c5217597676a9729f1b",
    'content-type': "application/json; charset=UTF-8",
    'cache-control': "no-cache",
    'retkey': "14",
    'logicret': "0",
    }
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
print(response.json())