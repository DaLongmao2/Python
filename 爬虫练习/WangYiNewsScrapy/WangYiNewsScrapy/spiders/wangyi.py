import scrapy
from selenium import webdriver
    from WangYiNewsScrapy.items import WangyinewsscrapyItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.wangyi.com']
    start_urls = ['https://news.163.com/']
    models_url = []  # 存储标题板块URI

    # 实例化浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'/home/zhangyi/chromedriver')

    # 解析首页板块标题
    def parse(self, response):
        li_list = response.xpath("//div[@class='ns_area list']/ul/li").getall()
        alist = [3, 4, 6, 7, 8]
        for index in alist:
            model_url = li_list[index].xpath("./a/@href").get()
            print(model_url)
            self.models_url.append(model_url)

        for url in self.models_url:
            yield scrapy.Request(url, callback=self.parse_model)

    # 每个版块的内容都是动态加载出来的相关内容 都是动态加载出来,
    def parse_model(self, response):
        div_list = response.xpath("//div[@class='ndi_main']/div")
        print(div_list)
        for div in div_list:
            title = div.xpath(".//div[@class='news_title']/h3/a/text()").get()
            new_url = div.xpath(".//div[@class='news_title']/h3/a/@href").get()
            print(new_url)

            item = WangyinewsscrapyItem()
            item['title'] = title
            yield scrapy.Request(new_url, callback=self.parse_newurl, meta={'item':item})

    def parse_newurl(self, response):
        info = response.xpath("//div[@class='post_text']/p/text()").getall()
        info = ''.join(info)
        item = response.mata['item']
        item['info'] = info

        yield item

    def closed(self, spiders):
        self.bro.quit()