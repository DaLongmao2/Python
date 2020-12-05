# coding = utf-8
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式
import urllib.request  # 制定网页,获取数据
import urllib.error  # 进行excel操作
import xlwt  # 进行SQLit数据进行操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    print(datalist)
    savepath = '豆瓣电影Top250.xls'
    # 保存数据
    saveDate(datalist, savepath)
    # askURL(baseurl)


# 创建正则表达式对象,表示规则
find_link = re.compile(r'<a href="(.*?)">')
find_title = re.compile(r'<span class="title">(.*?)</span>')
find_other = re.compile(r'<span class="other">(.*?)</span>')
find_bd = re.compile(r'<p class="">(.*?)</p>', re.S)
people = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 页数
        url = baseurl + str(i * 25)
        html = askURL(url)

        # 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all("div", class_="item"):
            # print(item)  # 测试查看电影 div itam
            data = []  # 保存一部电影的所有信息
            item = str(item)

            Link = re.findall(find_link, item)[0]  # 用来查找正则表达式查找制定的字符串
            data.append(Link)

            Title = re.findall(find_title, item)
            if len(Title) == 2:
                data.append(Title[0])
                str_title = Title[1].split()
                str_title.remove('/')
                data.append(''.join(str_title))
            else:
                data.append(Title[0])
                data.append(' ')

            bd = re.findall(find_bd, item)
            str_bd = bd[0].split()
            str_bd.remove('/')
            data.append(str_bd)
            # print(''.join(str_bd))

            People = re.findall(people, item)[0]
            data.append(People)

            # print(data)
            datalist.append(data)

    return datalist


# 得到指定URL的网页内容
def askURL(url):
    # 伪装
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
    }
    # 获取数据
    request = urllib.request.Request(url, headers=head)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveDate(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建book对象
    book_sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    cool = ('电影链接', '影片中文名', '影片英文名', '信息', '评分')
    for i in range(0, 5):
        book_sheet.write(0, i, cool[i])
    for i in range(0, 250):
        print('第%d条 数据....' % i)
        data = datalist[i]
        for j in range(0, 5):
            book_sheet.write(i + 1, j, data[j])
    book.save(savepath)


if __name__ == '__main__':
    main()
