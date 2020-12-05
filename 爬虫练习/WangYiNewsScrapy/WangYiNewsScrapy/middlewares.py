# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class WangyinewsscrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 这里的spider指的爬虫文件
    def process_response(self, request, response, spider):
        bro = spider.bro
        # 指定的响应对象进行篡改
        # 通过url指定request
        # 通过request指定response
        if request.url in spider.models_url:
            bro.get(request.url)
            page_text = bro.page_soure  # 包括了新的动态加载数据
            # 首页模块的response  进行篡改 将新的响应对象替换为新的响应对象
            # 基于 selenium 便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            # 首页板块的response
            return new_response
        # 其他的response
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
