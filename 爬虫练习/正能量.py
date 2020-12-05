# coding = utf-8
import multiprocessing

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式
import urllib.request  # 制定网页,获取数据
import urllib.error  # 错误捕获
import requests
import xlwt  # 进行Excel数据进行操作


# 爬取网页
def getData():
    # 调用 askURL 获取网页数据
    baseurl = "https://www.s888f.com/pic/html28/hhhhhhhaaaa"
    for i in range(2, 99):
        print('正在爬取第{}页数据'.format(i))
        url = baseurl + 'index_{}.html'.format(i)
        html = askURL(url)
        # 解析数据
        soup = BeautifulSoup(html, 'html.parser')
        # 获取指定内容
        for item in soup.find_all("div", class_="layout-box clearfix"):
            item = str(item)
            # 爬取规则
            Find_png = re.compile(r'<a class="video-pic loading" data-original="(.*?)".*?">')
            Png = re.findall(Find_png, item)
            for i in range(len(Png)):
                head = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
                }
                img_data = requests.get(url=Png[i], headers=head).content
                x = Png[i]
                filename = x.split('/')[-1]
                with open('png\\' + filename, mode='wb') as f:
                    f.write(img_data)
                    print('爬取成功 ' + x)
    # return datalist


# 得到指定的网页内容
def askURL(url):
    # 伪装
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    # 获取数据
    request = urllib.request.Request(url, headers=head)
    # 保存获取的数据
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


if __name__ == '__main__':
    getData()
