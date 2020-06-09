# -*- coding: utf-8 -*-
import logging

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
log = logging.getLogger(__name__)


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
