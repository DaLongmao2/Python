# coding = utf-8
import requests
import parsel
import os

base_url = 'http://book.zongheng.com/store/c{}/c0/b0/u0/p{}/v0/s9/t0/u0/i1/ALL.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
kai = False


def askurl(url):
    request = requests.get(url=url, headers=headers)
    request.encoding = request.apparent_encoding
    html = parsel.Selector(request.text)
    return html


def Book_info(url):
    book_title = url.xpath("//*[@id='readerFt']/div/div[2]/div[2]/text()").get()
    print(book_title)
    book_info = url.xpath("//*[@id='readerFt']/div/div[5]/p/text()").getall()
    book_info = ''.join(book_info)
    print(book_info)
    book_info_page = url.xpath("//div[@class='chap_btnbox']/a[@class='nextchapter']/@href").get()

    save_file(book_title, book_info)

    if str(book_info_page).split(':')[0] == 'http':
        book_page = askurl(book_info_page)
        Book_info(book_page)


def save_file(title, info):
    fp = open('《 {} 》.txt'.format(book_name), 'a+', encoding='utf-8')
    fp.write('{}\n{}\n{}\n'.format(title, ' -' * 50, info))
    fp.close()


print('我开始了')
for i in range(1, 999):
    book_list = ['全部', '奇幻玄幻', '武侠仙侠', '历史军事', '都市娱乐', '科幻游戏', '悬疑灵异', '竞技同人', '评论文集', '二次元']
    book_nam = [0, 1, 3, 6, 9, 15, 18, 21, 24, 40]
    dic = dict(map(lambda x, y: [x, y], book_list, book_nam))
    while True:
        x = input('请输入书的类型\n{}:\n '.format(book_list))
        if x in book_list:
            break
        print('类型不存在,请重新输入：')
    book_url_1 = askurl(base_url.format(dic[x], i)).xpath("//div[@class='bookname']/a/@href").getall()
    for url in book_url_1:
        book_url_2 = askurl(url).xpath("//div[@class='book-info']/div[@class='btn-group']/a/@href").get()
        print(book_url_2)
        book_url_3 = askurl(book_url_2)
        book_name = book_url_3.xpath('//*[@id="reader_warp"]/div[2]/a[3]/text()').get()
        print('《{}》'.format(book_name))
        Book_info(book_url_3)
