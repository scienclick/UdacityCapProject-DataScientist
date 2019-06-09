# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
import requests
import json

from .items import YahoocrawlerItem


class YahoocrawlerPipeline(object):
    def open_spider(self, spider):
        print("==============================================open")

    def close_spider(self, spider):
        print("==============================================close")



    def process_item(self, item, spider):
        if not isinstance(item, YahoocrawlerItem):
            return item

        print("==============================================process")
        print(item['title'])
        print(item['description'])
        print(item['datestr'])

        print("==============================================process")

        data = {
            "title": item['title'],
            "description": item['description'],
            "datestr": item['datestr'],

        }
        headers = {
            "Content-Type": "application/json",
        }

        r = requests.post("http://127.0.0.1:8000/news/", data=json.dumps(data), headers=headers)
        print(r.text)
        print(r.content)

        return item
