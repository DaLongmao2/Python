import scrapy


class BingdianItem(scrapy.Item):
    name = scrapy.Field()
    #小说名
    author = scrapy.Field()
    #作者
    novelurl = scrapy.Field()
    #小说地址
    serialstatus = scrapy.Field()
    #状态
    serialnumber = scrapy.Field()
    #连载字数
    category = scrapy.Field()
    #文章类别
    name_id = scrapy.Field()
    #小说编号


class DcontentItem(scrapy.Item):
    id_name = scrapy.Field()            #小说编号
    chaptercontent = scrapy.Field()     #章节内容
    num = scrapy.Field()
    chapterurl = scrapy.Field()
    chaptername = scrapy.Field()