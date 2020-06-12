# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 生成爬虫的命令 scrapy genspider -t crawl cibrc cibrc.gov.cn
class CibrcSpider(CrawlSpider):
    name = 'cibrc'
    allowed_domains = ['cibrc.gov.cn']
    start_urls = ['http://www.cbirc.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=zhengwuxinxi/xingzhengchufa.html&itemName=%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
