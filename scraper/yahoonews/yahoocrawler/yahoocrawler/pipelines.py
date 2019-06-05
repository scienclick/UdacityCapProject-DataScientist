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
        # hostname = 'localhost'
        # username = 'postgres'  # the username when you create the database
        # password = 'jhk1128f'  # change to your password
        # database = 'nnews1'
        # self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        # self.cur = self.connection.cursor()

    def close_spider(self, spider):
        print("==============================================close")

        # self.cur.close()
        # self.connection.close()

    def process_item(self, item, spider):
        if not isinstance(item, YahoocrawlerItem):
            return item

        print("==============================================process")
        print(item['title'])
        print(item['description'])
        print(item['datestr'])
        # self.cur.execute("insert into news_news(title,description,datestr) values(%s,%s,%s)",(item['title'],item['description'],item['datestr']))
        # self.connection.commit()
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

        # self.cur.execute("insert into news_news(title,description,datestr) values(%s,%s,%s)",(item['title'],item['description'],item['datestr']))
        # self.connection.commit()
        return item
