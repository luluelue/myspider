# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # name = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # title = response.xpath("//div[@class='tea_con']//h4/text()").extract()
        # describe = response.xpath("//div[@class='tea_con']//p/text()").extract()
        # print(name)
        # print(title)
        # print(describe)

        # 取结构化数据
        teachers = response.xpath("//div[@class='tea_con']//li")
        for li in teachers:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            item["describe"] = li.xpath(".//p/text()").extract_first()
            yield item

