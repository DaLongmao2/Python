import scrapy


class EbookSpider(scrapy.Spider):
    name = 'ebook'
    allowed_domains = ['www.soxscc.com']
    start_urls = ['https://www.soxscc.com/MangHuangJi/']

    def parse(self, response):
        passss