# -*- coding: utf-8 -*-
import scrapy


class TencenthrSpider(scrapy.Spider):
    name = 'tencenthr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%A4%8D%E7%89%A9%E5%A4%A7%E6%88%98%E5%83%B5%E5%B0%B82']

    def parse(self, response):
        title = response.xpath("//div [@class='correlation-degree']//a/h4/text()")
        print(title)
        pass
