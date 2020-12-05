from scrapy.pipelines.images import ImagesPipeline
import scrapy


class XiaohuascrapyPipeline:
    fp = None

    def open_spider(self, spider):
        print('爬虫开始...')
        self.fp = open('./xiaohua.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        img_name = item['img_name']
        print(img_name)
        img_src = item['img_src']
        print(img_src)
        self.fp.write('{}:{}\n'.format(img_name, img_src))
        return item

    def close_spider(self, spider):
        self.fp.close()


class imagesPipeline(ImagesPipeline):
        def get_media_requests(self, item, info):
            yield scrapy.Request(item['img_src'])

        def file_path(self, request, response=None, info=None):
            imgName = request.url.split('/')[-1]
            return imgName

        def item_completed(self, results, item, info):
            return item
