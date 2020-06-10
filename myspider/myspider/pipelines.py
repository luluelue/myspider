# -*- coding: utf-8 -*-
import logging
from myspider.items import ItcastItem
from pymongo import MongoClient

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
log = logging.getLogger(__name__)
client = MongoClient()
collection = client["itcast"]["teacher"]

class MyspiderPipeline:
    def process_item(self, item, spider):
        if spider.name == "itcast":
            log.info(item)
            item["itcast"] = "hello world"
        return item


class MyspiderPipeline1:
    def process_item(self, item, spider):
        if spider.name == "tencenthr":
            log.info(item)
        return item





class ItcastPipeline:
    def process_item(self, item, spider):
        if isinstance(item, ItcastItem):
            print("现在开始处理ITcast网站爬取的数据")
            # 爬取到的数据存储到MongoDB中
            collection.insert(dict(item))
            return item


