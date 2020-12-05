# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from ZongHengPro.spiders.zongheng import ZonghengSpider


class ZonghengproPipeline:
    fp = None

    def open_spider(self, spider):
        print('爬虫开始...')
        self.fp = open('./Books.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        print(title)
        info = item['info']
        print('= ' * 50)
        print(info)
        # file = '{}{}\\'.format(ZonghengSpider.books_file, ZonghengSpider.File)
        # self.fp.write('{} {} \n 《 {} 》\n {} \n'.format(file, '= ' * 50, title, info))
        self.fp.write('{} \n {} \n {}'.format(' =' * 50, title, info))
        return item

    def close_spider(self, spider):
        self.fp.close()
