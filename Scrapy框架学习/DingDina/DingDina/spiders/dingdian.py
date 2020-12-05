import scrapy


class DingdianSpider(scrapy.Spider):
    name = 'dingdian'
    # allowed_domains = ['www.x23us.net']
    start_urls = ['http://www.x23us.net/class/{}.html'.format(page) for page in range(2636)]

    def parse(self, response):
        response.xpath()