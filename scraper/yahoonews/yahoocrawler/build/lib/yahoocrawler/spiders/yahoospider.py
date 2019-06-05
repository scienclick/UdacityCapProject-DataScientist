# -*- coding: utf-8 -*-
import scrapy


class YahoospiderSpider(scrapy.Spider):
    name = 'yahoospider'
    allowed_domains = ['https://finance.yahoo.com/news']
    start_urls = ['https://finance.yahoo.com/news/']

    def parse(self, response):
        titles=response.xpath('//h3/a/text()').extract()
        highlights=response.xpath('//p[contains(@class,"")]/text()').extract()
        for title,highlight in zip(titles,highlights):
            yield {"title":title,
                   "highlight":highlight}
