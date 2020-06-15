# -*- coding: utf-8 -*-
import scrapy

# TODO 爬取12306网站登陆
class Spider12306Spider(scrapy.Spider):
    name = 'spider12306'
    allowed_domains = ['12306.cn']
    start_urls = ['http://12306.cn/']

    def parse(self, response):
        pass
