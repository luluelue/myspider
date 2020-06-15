# -*- coding: utf-8 -*-
import re

import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    # commit: Sign in
    # authenticity_token: TwXrRpeFL0zgKSaxKHQgjgHm7BoxtZKu1VexLzW1V5/5yx+WwzxSYVbyH4i42MAJ1wuHhvJXfFPrQkwpRQAngQ==
    # ga_id: 531765844.1592160106
    # login: 1132923539@qq.com
    # password:
    # webauthn-support: supported
    # webauthn-iuvpaa-support: supported
    # return_to:
    # required_field_402d:
    # timestamp: 1592161010257
    # timestamp_secret: f2d2d798c7410983b7896fc42def973360109045bbb3834328238e950d536b51
    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.pwd = None

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        # utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        post_data = dict(
            login="1132923539@qq.com",
            password=self.pwd,
            commit=commit,
            authenticity_token=authenticity_token,
            # ga_id=ga_id,
            # webauthn-support = "s",
            timestamp=str(timestamp),
            timestamp_secret=str(timestamp_secret),
            # utf8="utf8"
        )
        yield scrapy.FormRequest(
            url="https://github.com/session",
            formdata=post_data,
            method='POST',
            callback=self.parse_index
        )

    def parse_index(self, response):
        print(re.findall("lulu", response.body.decode()))
