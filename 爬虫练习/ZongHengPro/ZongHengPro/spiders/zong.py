import scrapy


class ZongSpider(scrapy.Spider):
    name = 'zong'
    # allowed_domains = ['zongheng.co']
    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v0/s9/t0/u0/i1/ALL.html']

    def parse(self, response):
