# coding = utf-8

import  requests
url = 'http://news.sina.com.cn/blank/hotnews_review.d.html?date=20200928'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text

print(html)