import scrapy


class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper'
    # allowed_domains = ['win4000.com/']
    start_urls = ['http://www.win4000.com/wallpaper.html']
    print('启动成功')

    def parse(self, response):
        div_all = response.xpath("//div[@class='main_cont']//ul[@class='clearfix']/li")
        for div in div_all:
            img_url = div.xpath(".//a/@href").extract_first()
            img_name = div.xpath(".//a/@title").extract_first()
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

            yield
            print(img_url, img_name)

