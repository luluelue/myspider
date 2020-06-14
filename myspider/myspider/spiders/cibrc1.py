# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 生成爬虫的命令 scrapy genspider -t crawl cibrc cibrc.gov.cn
from myspider.items import CbircVo


class CibrcSpider(scrapy.Spider):
    name = 'cibrc1'
    allowed_domains = ['cibrc.gov.cn']
    start_urls = [
        'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=4113,pageIndex=1,pageSize=18.json']


    # 详情页，api接口
    # http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectByDocId/data_docId=357905.json


    def parse(self, response):
        res = json.loads(response)
        item = CbircVo()

        if(res["rptCode"] == 200):
            total = res["data"]["total"]
            rows = res["data"]["rows"]
            for row in rows:
                docId = row["docId"]


