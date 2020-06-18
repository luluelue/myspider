# -*- coding: utf-8 -*-
import scrapy

# 无反爬机制
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html/']

    def parse(self, response):
        print(response)
        pass
