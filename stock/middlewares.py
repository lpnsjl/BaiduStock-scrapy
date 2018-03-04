# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from settings import USERAGENTS
from random import choice


class USERAGENTMiddleware(object):
    def process_request(self, request, spider):
        ua = choice(USERAGENTS)
        # print ua
        request.headers.setdefault('User-Agent', ua)