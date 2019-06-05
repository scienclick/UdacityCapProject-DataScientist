# -*- coding: utf-8 -*-
import scrapy
from ..items import YahoocrawlerItem


class AlphacrawlerSpider(scrapy.Spider):
    name = 'alphacrawler'
    allowed_domains = ['****.com']
    start_urls = ['***/market-news/all']

    def parse(self, response):
        DontAddStrings=["See","Previously:","Press Release","Source","Payable"]
        DontAddStrings2=["Relevant tickers include ","Forward yield"]
        listings = response.xpath('//li[@class="mc"]')

        for listing in listings:
            sym = listing.css('.media-left a::text').extract_first()
            title1 = listing.css('.title a::text').extract_first()
            newstime= listing.css('.item-date::text').extract_first()

            bullets= listing.xpath('.//*[@class="bullets"]/ul/li')
            desc=""


            # print(bullets)
            for bullet in bullets :
                print("-------------------------------")
                # bullet.css('.li ::text').extract_first()
                item=bullet.xpath('.//text()').extract()

                item=[y for y in item if not any (x in y for x in DontAddStrings)]

                # print(item)
                if not any(x in DontAddStrings2 for x in item):
                    desc=desc+''.join(item)

                # print(item)
                # print("*******************************")
            # text=quote.xpath('.//*[@class="text"]/text()').extract_first()


            # yield {'sym': sym,
            #        'title1': title1,
            #        'newstime':newstime,
            #        'desc':desc}
            yahoocrawleritem = YahoocrawlerItem(title=title1, description=desc, datestr=newstime)
            # yield {'sym': sym,
            #        'title1': title1,
            #        'newstime':newstime,
            #        'desc':desc}
            yield yahoocrawleritem
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url:
        #     yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

