#!/usr/bin/env python
# encoding: utf-8
import requests
import parsel

base_url = "https://www.soxscc.com/MangHuangJi/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

def geturl(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    html_xpath = parsel.Selector(response.text)

    return html_xpath

title_a_list = geturl(base_url).xpath("//div[@class='novel_list']/dl/dd")
for title_a in title_a_list:
    a_href = title_a.xpath("./a/@href").get()
    a_href = "https://www.soxscc.com" + a_href

    info = geturl(a_href)

    ebook_title = info.xpath('//div[@class="read_title"]/h1/text()').get()
    ebook_info = info.xpath('//div[@class="content"]//text()').getall()
    print(ebook_info)
    for i in ebook_info:
        print(i)
    if '您可以在百度里搜索' in ebook_info[0]:
        del ebook_info[0]
    ebook_info = " ".join(ebook_info)

    print(ebook_title)
    print(ebook_info)

# ['\n        \xa0\xa0\xa0\xa0您可以在百度里搜索“莽荒纪 搜小说(www.soxscc.com)”查找最新章节！\n        ', '\xa0\xa0\xa0\xa0新书名，叫《飞剑问道》，将在9月21号正式发布，14号开始预热活动，番茄也录制了视频，哈哈~~~~现在小说封面、简介都已上传，大家可以点击我的作者名‘我吃西红柿’找到新书，也可以在网站内直接搜索‘飞剑问道’，也能找到我的新书，大家可以先收藏下。\n', '\xa0\xa0\xa0\xa0*\n', '\xa0\xa0\xa0\xa0*        ', '莽荒纪最新章节地址：', 'https://www.soxscc.com/book/MangHuangJi.html', '\n\t\t', '莽荒纪全文阅读地址：', 'https://www.soxscc.com/MangHuangJi/', '\n\t\t', '莽荒纪txt下载地址：', 'https://www.soxscc.com/txt/MangHuangJi.html', '\n\t\t', '莽荒纪手机阅读：', 'https://m.soxscc.com/MangHuangJi/', '\n\t\t', '为了方便下次阅读，你可以点击下方的"收藏"记录本次（第1467章 番茄新书《飞剑问道》已经发布~~~）阅读记录，下次打开书架即可看到！', '\n\t\t', '喜欢《莽荒纪》请向你的朋友（QQ、博客、微信等方式）推荐本书，谢谢您的支持！！(www.soxscc.com)', '\n      ']