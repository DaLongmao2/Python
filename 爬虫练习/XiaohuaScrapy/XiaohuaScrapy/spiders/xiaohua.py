import scrapy
from XiaohuaScrapy.items import XiaohuascrapyItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/daxue/']

    def parse(self, response):
        div_list = response.xpath("//div[@class='container-fluid'][1]/div/div")
        for div in div_list:
            img_src = div.xpath("./div/a[1]/img/@src").get()
            img_name = div.xpath("./div/a[1]/img/@alt").get()
            item = XiaohuascrapyItem()
            item['img_src'] = img_src
            item['img_name'] = img_name
            yield item
        next_page = response.xpath("//div[@id='wrap']//nav//a[last()-2]/@href").get()
        print(next_page)
        if next_page:
            next_page = "http://www.xiaohuar.com" + next_page
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)