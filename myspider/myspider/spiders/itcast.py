# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        name = response.xpath("//div[@class='tea_con']//h3/text()")
        title = response.xpath("//div[@class='tea_con']//h4/text()")
        describe = response.xpath("//div[@class='tea_con']//p/text()")
        print(name)
        print(title)
        print(describe)
        pass
