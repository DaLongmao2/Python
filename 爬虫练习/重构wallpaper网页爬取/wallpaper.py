# coding = utf-8
import os
import shutil
import time
import requests
import parsel

# Begin_Url = 'http://www.win4000.com/wallpaper.html'  # 电脑
Begin_Url = 'http://www.win4000.com/mobile.html'  # 手机
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
filePath = r"E:\Img2"
if os.path.exists(filePath):
    print('该文件{}已经存在,5秒后删除'.format(filePath))
    time.sleep(5)
    shutil.rmtree(filePath)
os.mkdir(filePath)
print('已成功创建该文件夹 {}'.format(filePath))


def ask_url(url):
    """                                                         
    传入待请求的URI返回一个Selector对象
    :param url: 待请求的URI
    :return: Selector对象
    """
    response = requests.get(url=url, headers=Headers).text
    html = parsel.Selector(response)
    return html


def src_img(img_src):
    """
    传入待请求的图片URI返回二进制数据
    :param img_src: 待请求图片URI
    :return: 图片二进制数据
    """
    lmg_name = img_src.split('/')[5]
    img_data = requests.get(url=img_src, headers=Headers).content
    return img_data, lmg_name


def get_url(url):
    html = ask_url(url)
    html_list = html.xpath('//div[@class="box"]//a/@href').getall()
    print(html_list)  # 每个分类的url
    for item in html_list:
        print(item)
        url_1 = item.split('_')
        for pag in range(6):
            new_url_1 = "http://www.win4000.com/wallpaper_{}_0_0_{}.html".format(url_1[1], pag)
            html_2 = ask_url(new_url_1)
            html_list_2 = html_2.xpath('//div[@class="list_cont Left_list_cont"]//ul/li/a/@href').getall()
            for src_i in html_list_2:
                src_spl = src_i.split('.')
                html_3 = ask_url(src_i)
                html_3_title = html_3.xpath('//div[@class="ptitle"]/h1/text()').extract_first()
                html_3_em = html_3.xpath('//div[@class="ptitle"]/em/text()').extract_first()
                # http: // www.win4000.com / wallpaper_detail_173381_1.html
                path_1 = '{}\{}'.format(filePath, html_3_title)
                print('正在创建{}'.format(path_1))
                os.mkdir(path_1)
                for pag_1 in range(1, int(html_3_em) + 1):
                    new_url_2 = "http://www.win4000.{}_{}.html".format(src_spl[2], pag_1)
                    html_4 = ask_url(new_url_2)
                    img_src = html_4.xpath('//div[@class="pic-meinv"]/a/img/@src').extract_first()
                    # 下载图片
                    img_data_name = src_img(img_src)
                    with open(r'/home/zhangyi/.local/share/backgrounds/{}'.format(img_data_name[1]), 'wb') as fp:
                        fp.write(img_data_name[0])
                        print('成功写入{}'.format(img_data_name[1]))
                    # save_data(img_data_name[0], img_data_name[1], path_1)


# def save_data(img_data, img_name, path_1):
#     """
#     图片保存
#     :param img_data: 图片的二进制数据
#     :param img_name: 图片的名称
#     :param path_1: 图片的保存路径
#     :return: None
#     """
#     with open(r'{}\{}'.format(path_1, img_name), mode='wb') as f:
#         f.write(img_data)
#         print('正在保存' + img_name)


if __name__ == '__main__':
    get_url(Begin_Url)
