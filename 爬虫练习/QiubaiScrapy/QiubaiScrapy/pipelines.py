# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class QiubaiscrapyPipeline:
    fp = None

    def open_spider(self, spider):
        print('爬虫开始...')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        username = item['username']
        essay = item['essay']
        self.fp.write('{}\n:{}\n'.format(username, essay))
        return item

    def close_spider(self, spider):
        print('爬虫结束了...')
        self.fp.close()


class QiubaiscrapyPipeline_MySql:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='872039610', db='qiushi',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(
                'insert into qishiinfo values (null,"{}","{}");'.format(item['username'], item['essay'])
            )
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
