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


class ItcastPipeline:
    def process_item(self, item, spider):
        if isinstance(item, ItcastItem):
            print("现在开始处理ITcast网站爬取的数据")
            # 爬取到的数据存储到MongoDB中
            spider.collection.insert(dict(item))
            return item


class SunGvPipeline:
    # 此方法只会在爬虫启动前执行一次，爬虫是个全局对象，这里将连接对象放到spider对象中，使得每个有spider的地方都能够使用到这个连接对象
    # 后面最好在spider对象的初始化方法中声明，这样pycharm才能够智能提示
    # 开启mongodb命令 mongod -f G:\freeInstallSoft\mongodb-win32-x86_64-2012plus-4.2.8\mongodb.conf
    # 注册MongoDB为服务命令 mongod -f G:\freeInstallSoft\mongodb-win32-x86_64-2012plus-4.2.8\mongodb.conf --install
    # 停止MongoDB服务 net stop mongodb
    # 开启MongoDB服务 net start mongodb
    def open_spider(self, spider):
        client = MongoClient("localhost", 27017)
        spider.collection = client["sungv"]["item"]
        with open('pwd.txt', 'rt') as f:
            data = f.read()
            spider.pwd = data

    def process_item(self, item, spider):
        self.process_content(item["content"], item["title"])
        # 安装MongoDB
        # 存储到mongo中
        spider.collection.insert(dict(item))
        # print(item)
        return item

    def process_content(self, content, title):
        # \s表示空格 下面的正则表示将 \r\n 或者空格替换为空字符串
        # 去除空格和换行符
        if title == "常平新城市花园金都物业不作为，外人随意出入":
            print(content)

        if content is not None:
            content = [re.sub(r"\s", "", i) for i in content]
            content = [i for i in content if len(i) > 0]
