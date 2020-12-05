import requests
import parsel

baseurl = "http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v0/s9/t0/u0/i1/ALL.html"


def askurl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    response = requests.get(url=url, headers=headers).text
    response = requests.get(url=url, headers=headers).text
    # print(response)
    html = parsel.Selector(response)
    return html


def book_pag(url):
    html = askurl(url=url)
    url = html.xpath("//div[@class='bookimg']/a/@href").getall()
    print(url)
    for book_url in url:
        html = askurl(book_url)
        book_name = html.xpath("//div[@class='book-name']/text()").get()
        print('= ' * 100)
        print(book_name)
        url = html.xpath("//div[@class='btn-group']/a/@href").get()
        pag(url)


def pag(url):
    html1 = askurl(url)
    book_title = html1.xpath("//div[@class='title_txtbox']/text()").get()
    print(book_title)
    book_info = html1.xpath("//div[@class='content']/p/text()").getall()
    # for i in book_info:
    #     print(i)
    book_page_url = html1.xpath("//div[@class='chap_btnbox']/a[3]/@href").get()
    if book_page_url == 'javascript:void(0)':
        print('= ' * 100)
        return None
    pag(book_page_url)


if __name__ == '__main__':
    for i in range(1, 1000):
        # time.sleep(3)
        print(baseurl.format(i))
        book_pag(baseurl.format(i))
