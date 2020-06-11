# -*- coding: utf-8 -*-
import scrapy
from myspider.items import SunVo
import urllib.parse as urlparse


# 运行爬虫不要开代理！！
class SungvSpider(scrapy.Spider):
    name = 'sunGV'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    # //表示无视层级关系，/ 表示重视层级关系，一层层解析
    def parse(self, response):

        li_list = response.xpath("//ul[@class='title-state-ul']/li")
        host = 'http://wz.sun0769.com'
        for li in li_list:
            item = SunVo()
            item["title"] = li.xpath("./span[@class='state3']/a/text()").extract_first()
            item["href"] = host + li.xpath("./span[@class='state3']/a/@href").extract_first("")
            item["publish_time"] = li.xpath("./span[5]/text()").extract_first()

            yield scrapy.Request(
                item['href'],
                # 用回调函数来处理详情页
                callback=self.parse_detail,
                # 用来给回调函数传递数据
                meta={"item": item}
            )

        next_url = host + response.xpath("//a[@class='arrow-page prov_rota']/@href").extract_first()
        next_page = urlparse.parse_qs(urlparse.urlparse(next_url).query).get("page")
        current_page = response.meta.get("next_page", 1)
        print("当前页", current_page)
        print("下一页", next_page)
        if next_url is not None and current_page != next_page:
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                meta={"next_page": next_page}
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='details-box']/pre/text()").extract_first()
        item["content_img"] = response.xpath(
            "//div[@class='clear details-img-list Picture-img']/img/@src").extract()
        # yield 完成之后交给pipeline处理
        yield item
