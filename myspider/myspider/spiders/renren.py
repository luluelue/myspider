# -*- coding: utf-8 -*-
import re

import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/853339429']

    # 重写爬虫的初始请求方法，制造产生cookie再执行后面的请求动作
    def start_requests(self):
        # 注意：scrapy的cookie必须放在cookies中，不能放在header中，会无法识别
        cookies = "anonymid=kbfe8z0nkdorlh; depovince=GUZ; jebecookies=199393a8-65a4-46d2-bb06-278dd9ca9e5f|||||; _r01_=1; ick_login=7f39282f-0e5d-4c0b-8379-820bedc1dc68; taihe_bi_sdk_uid=b2d06161ed642d613a283cd2d6f02847; taihe_bi_sdk_session=06906dd9ab2eabe921f29cb038cfef4d; _de=697ADF65ECA62DA66870B098DE4AEE7E; p=cda2fd1da5dcb1c5022adfc49a83097a9; first_login_flag=1; ln_uact=13368069866; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=f2b431229f148c908f39db4a9c7664279; societyguester=f2b431229f148c908f39db4a9c7664279; id=853339429; xnsid=4bf02226; ver=7.0; loginfrom=null; jebe_key=440d8542-b946-4c6c-950a-14647b8ca5ec%7C59d8cd5374e8d2932e29f5fd048f4f58%7C1592158840729%7C1%7C1592158840782; wpsid=15879339345850; wp_fold=0; _ga=GA1.2.550207978.1592158850; _gid=GA1.2.1524899057.1592158850"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("9866", response.body.decode()))
