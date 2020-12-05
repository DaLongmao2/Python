# coding = utf-8
import time

import parsel
import requests
import lxml.html

base_url = 'https://m.51job.com/search/joblist.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'}


def pag_url(i):
    data = {
            "keyword": "python",
            "keywordtype": 2,
            "jobarea": "000000",
            "pageno": i
    }

    print(data)
    s = requests.get(base_url, data, headers=headers)
    tree = lxml.html.fromstring(s.content)
    url = s.url
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    html = parsel.Selector(r.text)
    pag_urls = html.xpath('//div[@class="items"]//a/@href').getall()
    # print(pag_urls)
    return pag_urls


def get_url():
    """
    获取每页的数据
    :return:
    """
    data = []
    for i in range(1):
        info = []
        for j in pag_url(1):
            # print(info)
            print(j)
            info_list = []
            data = {
                "rc": "03"
            }
            # requests.packages.urllib3.disable_warnings()
            time.sleep(2)
            request = requests.get(url=j, data=data, headers=headers)
            request.encoding = request.apparent_encoding
            # print(request.text)
            html = parsel.Selector(request.text)
            title_envelope = html.xpath("//div[@class='jbox']//p/text()").getall()
            if len(title_envelope) != 2:
                print(j)
                print(title_envelope)
                print('数据有问题')
            else:
                x = [info_list.append(i) for i in title_envelope]
                info.append(x)
            # 获取到岗位需要人数  地址  最低学历   工作经历
            address = html.xpath("//div[@id='pageContent']/div[1]/div[1]/div[2]/div[1]/span/text()").getall()
            if len(address) != 4:
                print(j)
                print(address)
                print('数据有问题')
            else:
                x = [info_list.append(i) for i in address]
                info.append(x)
            print(info_list)
            info.clear()
            # info.append(info_list)


if __name__ == '__main__':
    get_url()
