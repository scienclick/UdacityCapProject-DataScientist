# -*- coding: utf-8 -*-
import scrapy


class YahoospiderSpider(scrapy.Spider):
    name = 'yahoospider'
    allowed_domains = ['***']
    start_urls = ['****']

    def parse(self, response):
        # titles=response.xpath('//h3/a/text()').extract()
        titles=response.xpath('//*[@class="StrechedBox"]/text()').extract()
        highlights=response.xpath('//p[contains(@class,"")]/text()').extract()
        for title,highlight in zip(titles,highlights):
            yield {"title":title,
                   "highlight":highlight}
