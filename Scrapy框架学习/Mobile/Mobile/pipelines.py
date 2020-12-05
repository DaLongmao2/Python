# Define your item pipelines here
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#
#
# class MobilePipeline:
#     conn = None
#     cursor = None
#
#     def open_spider(self, spider):
#         self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='1122', db='src_img',
#                                     charset='utf8')
#
#     def process_item(self, item, spider):
#         self.cursor = self.conn.cursor()
#         try:
#             self.cursor.execute(
#                 'insert into imgsrc values ("{}");'.format(item['png_src'])
#             )
#             self.conn.commit()
#             print('保存成功 {}'.format(item['png_src']))
#         except Exception as e:
#             print(e)
#             self.conn.rollback()
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()


class imagesPipeline(ImagesPipeline):
    a = 1
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['png_src'])

    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]
        self.a += 1
        print("{}、正在保存{}".format(self.a, imgName))
        return imgName

    def item_completed(self, results, item, info):
        return item