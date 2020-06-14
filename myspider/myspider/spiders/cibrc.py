# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 生成爬虫的命令 scrapy genspider -t crawl cibrc cibrc.gov.cn
class CibrcSpider(CrawlSpider):
    name = 'cibrc'
    allowed_domains = ['cibrc.gov.cn']
    start_urls = [
        'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=4113,pageIndex=2,pageSize=18.json']

    # /cn/view/pages/ItemDetail.html?docId={{x.docId}}&itemId={{x.itemId}}
    rules = (
        Rule(LinkExtractor(allow=r'/cn/view/pages/ItemDetail.html?docId=\.*&itemId={{x.itemId}}'),
             callback='parse_item'),

    )

    def parse_item(self, response):
        item = {}
        title = response.xpath("//div[@class='wenzhang-title ng-binding']/text()").extract_first()
        print(title)
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
