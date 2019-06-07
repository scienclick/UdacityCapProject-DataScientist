# -*- coding: utf-8 -*-
import scrapy


class WordolicrawlerSpider(scrapy.Spider):
    name = 'wordolicrawler'
    allowed_domains = ['****']
    start_urls = ['****']

    def parse(self, response):
        news = response.css('.article a::text').extract()
        date = response.css('.news-date::text').extract()

        for anews,adate in zip(news,date) :
            yield {"date":adate,"news":anews}


        # next_page_url =  response.xpath('//*[(@id = "ContentPlaceHolderDefault_mainContent_btnNext")]/@href').extract_first()
        # if next_page_url:
        #     yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)