# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 股票名
    name = scrapy.Field()
    # 收盘价
    close_price = scrapy.Field()
    # 开盘价
    open_price = scrapy.Field()
    # 当前价
    cur_price = scrapy.Field()
    # 最高价
    highest_price = scrapy.Field()
    # 最低价
    lowest_price = scrapy.Field()
    # 成交量
    volume = scrapy.Field()
    # 换手率
    change_rate = scrapy.Field()
