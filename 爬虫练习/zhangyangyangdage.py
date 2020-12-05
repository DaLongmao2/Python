# coding = utf-8
import requests
import parsel

url = 'http://www.win4000.com/zt/yingxionglianmeng.html'
response = requests.get(url=url).text
html = parsel.Selector(response)
img_url_a = html.xpath("//div[@class='tab_box']//a/@href").getall()
print(img_url_a)
i = 1
for url in img_url_a:
    response1 = requests.get(url).text
    html1 = parsel.Selector(response1)
    jpg_url = html1.xpath("//div[@class='pic-meinv']//img/@src").get()
    print(jpg_url)
    jpg = requests.get(jpg_url).content


    print(i)
    with open('图片{}.jpg'.format(i), 'wb') as fp:
        fp.write(jpg)
        print('保存成功', i)
    i += 1
