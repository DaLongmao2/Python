# coding = utf-8
# coding = utf-8
import requests
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式
import urllib.request  # 制定网页,获取数据
import urllib.error  # 进行excel操作
import xlwt  # 进行SQLit数据进行操作

# baseurl = "https://cn.pornhub.com/video/search?search=pornhud+sex"
baseurl = "https://hw-cdn2.adtng.com/a7/creatives/51/1270/809738/961496/961496_video_with_sound.mp4"
# 爬取网页
# datalist = getData(baseurl)
# print(datalist)
# savepath = '豆瓣电影Top250.xls'
# # 保存数据
# saveDate(datalist, savepath)


# 伪装
head = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Mobile Safari/537.36"
}
# 获取数据
# response = requests.get(url=baseurl, headers=head)
# response.encoding = response.apparent_encoding
# html = response.text


img_data = requests.get(url=baseurl, headers=head).content

print('开始保存')
file_name = baseurl.split('/')[-1]
print(file_name)
with open('hha\\' + file_name, mode='wb') as f:
    f.write(img_data)
    print('正在保存' + file_name)
