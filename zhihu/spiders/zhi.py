# -*- coding: utf-8 -*-
import scrapy


class ZhiSpider(scrapy.Spider):
    name = "zhi"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
