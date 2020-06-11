# -*- coding: utf-8 -*-
import logging
import pymongo
from myspider.items import ItcastItem
from pymongo import MongoClient
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
log = logging.getLogger(__name__)
client = MongoClient("localhost", 27017)
collection = client["sungv"]["item"]


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


class SunGvPipeline:
    def process_item(self, item, spider):
        self.process_content(item["content"], item["title"])
        # 安装MongoDB
        # 存储到mongo中
        collection.insert(dict(item))
        # print(item)
        return item

    def process_content(self, content, title):
        # \s表示空格 下面的正则表示将 \r\n 或者空格替换为空字符串
        # 去除空格和换行符
        if title=="常平新城市花园金都物业不作为，外人随意出入":
            print(content)

        if content is not None:
            content = [re.sub(r"\s", "", i) for i in content]
            content = [i for i in content if len(i) > 0]
