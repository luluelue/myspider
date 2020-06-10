# -*- coding: utf-8 -*-


import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    title = scrapy.Field()
    position = scrapy.Field()


class SunVo(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    publish_time =scrapy.Field()
    content_img =scrapy.Field()
    content =scrapy.Field()
