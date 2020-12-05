import scrapy
from BiQuGe.items import BiqugeItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    # allowed_domains = ['www.biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/xuanhuan/']

    def parse(self, response):
        li_list = response.xpath("//div[@id='newscontent']/div/ul/li")
        for li in li_list:
            a_href = li.xpath("./span/a/@href").get()
            url = "https://www.biquge.com.cn/" + a_href
            # print(url)
            yield scrapy.Request(url, callback=self.book)


    def book(self, response):
        book_title_url = response.xpath("//div[@class='box_con']//dd/a/@href").getall()
        for url in book_title_url:
            url = "https://www.biquge.com.cn" + url
            # print(url)
            yield scrapy.Request(url, callback=self.book_info)


    def book_info(self, response):
        print(response.url)
        book_name = response.xpath("//div[@class='con_top']/a[3]/text()").get()
        book_title = response.xpath("//div[@class='bookname']/h1/text()").get()
        book_info = response.xpath('//*[@id="content"]/text()').getall()
        # print(book_name)
        # print(book_title)
        # print(book_info)
        info = ''
        for i in book_info:
            x = i.strip()
            info += x
        # print(info)

        item = BiqugeItem()
        item['book_name'] = book_name
        item['book_title'] = book_title
        item['book_info'] = book_info

        yield item