# 使用 requests 获取网页
#     parsel 解析网页
#
# 1、确定爬取的url地址(分析网页的性质 静态网页/动态网页)
# 2、发送请求 -- requests (范数据 <文本\url地址\css\js>)
# 3、数据解析 -- 解析出我们想要的内容(数据)
# 4、保存数据

import time
import requests
import parsel
import multiprocessing


# 入口函数http://www.win4000.com/wallpaper_2285_0_0_1.html
def main():
    base_url = 'http://www.win4000.com/wallpaper_0_0_0_{}.html'
    # base_url = 'http://www.win4000.com/wallpaper_2285_0_0_{}.html'
    # ask_url(base_url)
    get_url(base_url)


# 数据获取
def ask_url(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    # time.sleep(1)
    try:
        response = requests.get(url=base_url, headers=headers)
        response.encoding = response.apparent_encoding
        html_data = response.text
        return html_data, headers
    except:
        pass


# 数据解析
def get_url(base_url):
    for page in range(1, 6):
        print(page)
        # 转换为Selector对象。
        url = base_url.format(page)
        data = ask_url(url)
        html = parsel.Selector(data[0])
        data_list = html.xpath('//div[@class="tab_box"]//ul/li/a/@href').get_all()
        # print(data_list)
        # 每张图片内部 链接 地址 URL
        for item_url in data_list:
            data2 = ask_url(item_url)
            # 每张图片内部 链接 地址 URL 内部 Html 文件  -—> data2
            # print(data2)
            data2_html = parsel.Selector(data2[0])  # 转换为Selector对象
            data2_ptitle_h1 = data2_html.xpath('//div[@class="ptitle"]/h1/text()').getall()
            # 爬取 data2 中的 标题内容 h1
            # print(data2_ptitle_h1)
            data2_ptitle_em = data2_html.xpath('//div[@class="ptitle"]/em/text()').getall()
            # print(data2_ptitle_em)
            # 爬取 data2 中的 页数 内容
            # http://www.win4000.com/wallpaper_detail_173111_1.html
            item_split = item_url.split('.')

            page = 1
            while page < int(data2_ptitle_em[0]):
                # for em in range(1, int(data2_ptitle_em[0])):
                # 拼接新的内部url分页地址
                new_url = "{}.{}.{}_{}.html".format(
                    item_split[0], item_split[1], item_split[2], page
                )
                # print(new_url, 'new')
                data3_html = ask_url(new_url)
                data4_html = parsel.Selector(data3_html[0])
                # print(data3_html)
                img_url = data4_html.xpath('//div[@class="pic-meinv"]/a/img/@src').get()
                print(img_url, 'ha')
                img_data = requests.get(url=img_url, headers=data3_html[1]).content
                print(img_data)
                save_file(img_data, img_url)
                page += 1
            # 此处是爬取 每张图片的
        # try:
        #     for i in data_list:
        #         response = requests.get(url=i, headers=data[1]).text
        #         html2 = parsel.Selector(response)
        #         img_url = html2.xpath('//div[@class="pic-meinv"]/a/img/@src').get()
        #         print(img_url)
        #         img_data = requests.get(url=img_url, headers=data[1]).content
        #         print(img_data)
        #         save_file(img_data, img_url)
        # except:
        #     print('爬取失败')


# 保存数据
def save_file(img_data, img_url):
    print('开始保存')
    file_name = img_url.split('/')[-1]
    print(file_name)
    with open('png\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('正在保存' + file_name)


if __name__ == '__main__':
    main()
