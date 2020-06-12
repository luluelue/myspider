# -*- coding: utf-8 -*-
import scrapy
import fake_useragent

ua = fake_useragent.UserAgent()


class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%9A%8F%E6%9C%BA%E6%95%B0']

    def parse(self, response):
        print('us------------------>',response.request.headers["User-Agent"], '\n')
        response.xpath("//div[@class='feed welcome__feed']")
        pass
