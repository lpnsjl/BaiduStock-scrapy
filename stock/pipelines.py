# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo


class StockPipeline(object):
    """def __init__(self):
        self.filename = open('stock.json', 'w')

    def process_item(self, item, spider):
        # print item
        data = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(data.encode('utf-8'))
        return item

    def close_spider(self):
        self.filename.close()"""
    def process_item(self, item, spider):
        """
        将数据存入mongodb数据库中
        """
        # mongod数据库的主机号
        host = '127.0.0.1'
        # 端口号
        port = 27017
        # 数据库名称
        dbname = 'baidustock'
        # 表名称
        sheetname = 'gupiaodata'
        # 创建一个数据库客户端
        mongoClient = pymongo.MongoClient(host=host, port=port)

        # 创建数据库与表
        db = mongoClient[dbname]
        sheet = db[sheetname]

        # 将股票数据插入表中
        sheet.insert(dict(item))

        return item




