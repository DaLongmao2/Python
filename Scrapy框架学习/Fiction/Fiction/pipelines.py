# -*- coding: utf-8 -*-
import os


class FictionPipeline(object):

    def process_item(self, item, spider):
        curPath = '/home/zhangyi/全书网小说'
        tempPath = str(item['name'])
        targetPath = curPath + os.path.sep + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        filename_path = '/home/zhangyi/全书网小说' + os.path.sep + str(item['name']) + os.path.sep + str(item['chapter_name']) + '.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['chapter_content'] + "\n")
        return item

    # def process_mysql(self, spider):
    #     pass