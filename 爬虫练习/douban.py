# coding = utf-8
import requests
import parsel

# 1、定义开始 URI
start_url = 'http://www.win4000.com/wallpaper_192_0_0_1.html'
# 2、定义UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
# 3、request.get() 请求网页 传入 ulr, headers 信息 —> 得到一个Response对象
#       .text  请求到的数据转换为 字符串
#       .content 请求到的数据转换为 二进制
response = requests.get(url=start_url, headers=headers).text

# 4、使用parsel.Selector()来转换Selector对象,进行Xpath匹配(Xpath只能匹配Selector对象的数据) 传入刚得到的 response
html = parsel.Selector(response)

# 5、转换后使用Xpath进行匹配图片的链接
#       .getall() 匹配所有符合规则的 返回一个 list
#       .first() 匹配符合规则的第一个 返回一个 str
img_url = html.xpath(
    '//div[@class="main"]//div[@class="w1180 clearfix"]//div[@class="tab_box"]//ul/li/a/img/@data-original').getall()
print(img_url)

# 6、遍历img列表获取所有匹配到的所有img链接
i = 1
for img_url in img_url:
    print('正在爬取{}'.format(img_url))

    # 7、请求得到的 img 的 url 地址 并且 转换为 二进制(.content) 数据
    img = requests.get(url=img_url, headers=headers).content
    img_name = '图片{}.png'.format(i)
    print(img_name)

    with open(img_name, 'wb') as fp:
        #  8、将获取到的 img 二进制 写入文件
        fp.write(img)
        i += 1

print('爬取完成')
