# -*- coding: utf-8 -*-
import scrapy

# 无反爬机制，可直接获取数据
class TiebaSpider(scrapy.Spider):

    def start_requests(self):
        # 注意：scrapy的cookie必须放在cookies中，不能放在header中，会无法识别
        cookies = "BAIDUID=6634E787DB850D07E13B290432785467:FG=1; TIEBAUID=e7d5aa4e4260f3fcd6d4935d; TIEBA_USERTYPE=360a690fe7b3832a991df501; BIDUPSID=6634E787DB850D07E13B290432785467; PSTM=1588227312; bdshare_firstime=1590422266122; H_WISE_SIDS=147719_147117_147207_142018_148320_147090_147893_148194_148867_147681_148434_147279_146537_148002_148823_147849_148644_147830_148438_148754_147888_146574_148523_149175_127969_147238_146551_147024_146732_138425_148537_131423_145937_128700_142205_147527_146899_107318_147136_148940_140312_144966_145607_139883_148345_148048_148422_145395_148868_110085; st_key_id=17; BDRCVFR[abe9uUBlp-C]=mk3SLVN4HKm; H_PS_PSSID=31729_1430_21123_32045_30824; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1591895084,1592244701,1592329990,1592415525; wise_device=0; 706969881_FRSVideoUploadTip=1; IS_NEW_USER=04e8865453260a42b0a22c4e; BAIDU_WISE_UID=wapp_1592416687594_773; USER_JUMP=-1; CLIENTWIDTH=736; CLIENTHEIGHT=1000; pb_prompt=1; SET_PB_IMAGE_WIDTH=716; baidu_broswer_setup_lu1132923539=0; SEENKW=%E6%A4%8D%E7%89%A9%E5%A4%A7%E6%88%98%E5%83%B5%E5%B0%B82%23%CE%F7%C4%CF%B4%F3%D1%A7; LASW=414; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1592417616; st_data=115aaee954101b5de3aca30adbe4037f5810c6892dfd747ddf593b2c81ec72b0f1721c0c78619da4f056a95a3caa6c5ff65e5b2d6a7e99aadd00abf298b7dbddb559da7fab9f59cc6cd0b7b8e47264e5f189fbadb5e071b16233be0f67c1bc4aea9830228448c2924965735f439f44fe33bd78951fe1df962c34e25a5a777833; st_sign=afbb7410"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )


    name = 'tieba'
    allowed_domains = ['baidu.com']
    start_urls = [
        'https://tieba.baidu.com/f?kw=%E6%A4%8D%E7%89%A9%E5%A4%A7%E6%88%98%E5%83%B5%E5%B0%B82&fr=index&fp=0&ie=utf-8']

    def parse(self, response):
        print(response.headers)
        title_list = response.xpath("//a[@rel='noreferrer']")
        for title in title_list:
            item = {}
            item["href"] = title.xpath("./@href")
            item["title"] = title.xpath("./text()")
            print(item)
