# coding = utf-8
import requests

for i in range(0, 481):
    url1 = "https://m3u8.46cdn.com/videos/202004/erikKwiU/hls/erikKwiU"
    url2 = str(i) + ".ts"
    url = url1 + url2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    x = url.split('/')
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    with open('hha\\' + x[-1], 'wb') as f:  # 文件的打开和保存
        f.write(r.content)
        print("第{}文件保存成功".format(i))