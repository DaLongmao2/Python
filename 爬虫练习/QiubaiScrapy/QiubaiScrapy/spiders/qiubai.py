import scrapy
from QiubaiScrapy.items import QiubaiscrapyItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    # 终端
    # def parse(self, response):
    #     div_list = response.xpath("//div[@class='col1 old-style-col1']/div")
    #     all_data = []
    #     for div in div_list:
    #         username = div.xpath(".//a[2]/h2/text()")[0].get()
    #         essay = div.xpath(".//a/div/span[1]//text()").getall()
    #         essay = ''.join(essay)
    #
    #         item = {
    #             'username': username,
    #             'essay': essay
    #         }
    #
    #         all_data.append(item)
    #     return all_data

    # 管道
    def parse(self, response):
        div_list = response.xpath("//div[@class='col1 old-style-col1']/div")
        for div in div_list:
            username = div.xpath(".//a[2]/h2/text()")[0].get()
            essay = div.xpath(".//a/div/span[1]//text()").getall()
            essay = ''.join(essay)

            item = QiubaiscrapyItem()
            item['username'] = username
            item['essay'] = essay

            yield item  # 将item提交给管道

# 新建项目文件 scrapy stratproject <项目名>
# 创建爬虫文件 scrapy genspider <爬虫名称> <域名>
# 启动爬虫 scrapy crawl <爬虫名>
# LOG_LEVEL = 'ERROR' 只显示错误信息

# 持久化存储
# 终端
#   - 只可以将 parse 方法中的返回值存储到本地
#   - scrapy crawl <爬虫名> -o <路径>
# 管道
#   - 解析数据
#   - 在 item 类中定义相关属性
#   - 将解析的封装存储到item类型对象中
#   - 将 item 类型的对象交给管道进行持久化的操作
#   - 在管道类的 process_item 中将其接受到的 item 对象中存储的数据进行持久化的存储
#   - 在配置中开启管道

# 管道存在优先级  优先级数字越低代表越优先
# item 会将数据交给优先级最高的管道进行处理
# 如果启用第二个管道 需要在第一优先级处理完后 return item 将数据转交给第二优先级管道处理

