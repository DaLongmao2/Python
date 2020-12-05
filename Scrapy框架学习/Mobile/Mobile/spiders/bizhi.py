import scrapy
from Mobile.items import MobileItem

png_type = [i for i in range(2338, 2357)]
png_type_2 = [2359, 2360, 2362]
y = png_type + png_type_2


class BizhiSpider(scrapy.Spider):
    name = 'bizhi'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/mobile_{}_0_0_{}.html'.format(j, i) for i in range(1, 6) for j in y]

    def parse(self, response):
        png_url_list = response.xpath("//div[@class='tab_box']/div/ul/li")
        for url in png_url_list:
            request_png_url = url.xpath("./a/@href").get()
            yield scrapy.Request(request_png_url, callback=self.png_request)

    def png_request(self, response):
        png_page = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]/em/text()').get()
        # print(response.url)
        png_page_url = response.url
        png_page_list = png_page_url.split('.')
        for page in range(1, int(png_page) + 1):
            png_page_new_url = 'http://www.win4000.{}_{}.html'.format(png_page_list[2], page)
            print(png_page_new_url)
            yield scrapy.Request(png_page_new_url, callback=self.png)

    def png(self, response):
        img_url = response.xpath("//div[@id='pic-meinv']/a/img/@src").get()
        print(img_url)
        itme = MobileItem()
        itme['png_src'] = img_url

        yield itme
