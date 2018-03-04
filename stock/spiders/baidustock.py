# -*- coding: UTF-8 -*-
import scrapy
import re
from stock.items import StockItem
from random import choice

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['http://quote.eastmoney.com', 'gupiao.baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']


    def parse(self, response):
        stock_codes = re.findall(r'a target="_blank" href="http://quote.eastmoney.com/(.*?).html">', response.text)
        # print stock_codes
        for stock_code in stock_codes:
            stock_url = 'https://gupiao.baidu.com/stock/%s.html' % stock_code
            #print stock_url


            headers = {#'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
                       #'Host': 'gupiao.baidu.com',
                       #'Cookie': 'BAIDUID=F6E05707D9608A9A7377CC41A9786C93:FG=1; PSTM=1513595439; BIDUPSID=928AC9EF735A6296F00B601867662D9C; BDSFRCVID=nZLsJeC62lPzK3rAOoz9U1b4smyBpBOTH6aoGcYCMEL0kdi0ZCeMEG0Pqx8g0KubhqFqogKKXgOTHw3P; H_BDCLCKID_SF=tJPDoKL-tK_3fP36q4J2jjv-qxby26nubI3eaJ5nJDoSV-coDn5NXP4hLn_D5j3ea65GQpovQpP-HJ7j-prTXfLTDMRba6Oz0KTuKl0MLPjWbb0xynoDMb_zKfnMBMnv52OnaP0bLIFKMKDRj6K5D6PW5ptXKb8tfnKX3b7EfbrA8-O_bf--D4Ar244ebfo9a5L8-CjtJPOVJqoxLxnxy5K_hPJ2XxJu3mtjBbbVtUcTeq6HQT3mKJvbbN3i-4j3-mcDWb3cWMnJ8UbS5Tbme4tX-NFDt60ttU5; pgv_pvi=7384993792; pgv_si=s1072037888; PSINO=3; H_PS_PSSID=1420_21091_25177; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_35d1e71f4c913c126b8703586f1d2307=1513942999,1513944500,1513944530,1514525108; Hm_lpvt_35d1e71f4c913c126b8703586f1d2307=1514554871',
                       #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       #'Cache-Control': 'max-age=0',
                       #'Connection': 'keep-alive',
                       #'Upgrade-Insecure-Requests': '1',
                       #'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Referer': 'https://gupiao.baidu.com/'}
            yield scrapy.Request(stock_url, callback=self.parse_page, headers=headers)

    def parse_page(self, response):
        try:
            item = StockItem()

            # 股票名
            item['name'] = response.xpath('//a[@class="bets-name"]/text()').extract()[0].strip()[:4]
            # 收盘价
            item['close_price'] = response.xpath('//div[@class="line2"]//dl[1]/dd/text()').extract()[0]
            # 开盘价
            item['open_price'] = response.xpath('//div[@class="line1"]//dl[1]/dd/text()').extract()[0]
            # 当前价
            item['cur_price'] = response.xpath('//strong/text()').extract()[0]
            # 最高价
            item['highest_price'] = response.xpath('//div[@class="line1"]/dl[3]/dd/text()').extract()[0]
            # 最低价
            item['lowest_price'] = response.xpath('//div[@class="line2"]/dl[3]/dd/text()').extract()[0]
            # 成交量
            item['volume'] = response.xpath('//div[@class="line1"]/dl[2]/dd/text()').extract()[0]
            # 换手率
            item['change_rate'] = response.xpath('//div[@class="line2"]/dl[2]/dd/text()').extract()[0]

            yield item
        except:
            pass


