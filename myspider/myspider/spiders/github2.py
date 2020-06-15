# -*- coding: utf-8 -*-
import re

import scrapy


# 登陆GitHub的进阶版本，能够自动获取form表单
class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.pwd = None

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            # 自动从response中寻找form表单，若有多个form，也可以指定xpath等属性来定位表单
            response,
            # 这里需要使用标签的name值作为key
            formdata={"login": "1132923539@qq.com", "password": self.pwd},
            callback=self.deal_cookie
        )

    def deal_cookie(self, response):
        print(re.findall("lulu",response.body.decode()))
