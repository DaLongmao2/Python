from itemadapter import ItemAdapter
import pymysql


class BiqugePipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('爬虫开始了...')
        self.conn = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='1122',
            db='tests',
            charset='utf8'
        )
        print(self.conn)
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        book_title = item.get('book_title')
        book_info = ""
        for info in item.get('book_info'):
            book_info += info.replace('\n', '').replace('\r', '').strip()
        try:
            # self.cursor.execute('INSERT INTO navel values ("null", "{book_title}", "{book_info}")')
            sql = 'INSERT INTO navel values (null, "{}", "{}");'.format(book_title, book_info)
            self.cursor.execute(sql)
            self.conn.commit()
            print('提交了')
        except Exception as e:
            print(e)
            self.conn.rollback()

            print('回滚了')
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('爬虫结束了...')
