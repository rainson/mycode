# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import pandas as pd

class NjHousePipeline(object):
    columns = ["area", "house", "houseroom", "totalprice", "unitprice" ]
    def open_spider(self, spider):
        # self.con = sqlite3.connect("ershoufang.sqlite")
        # self.cu = self.con.cursor()
        self.data = pd.DataFrame(columns=self.columns)

    def process_item(self, item, spider):
        # print(spider.name, "pipelines")
        # house = scrapy.Field()
        # house_area = scrapy.Field()
        # unit_price = scrapy.Field()
        # total_price = scrapy.Field()
        # house_room = scrapy.Field()
        # insert_sql = "insert into ershoufang (area, house, houseroom, totalprice, unitprice ) values('{}','{}','{}','{}','{}')".format(
        #     item["house_area"],
        #     item["house"],
        #     item["house_room"],
        #     item["total_price"],
        #     item["unit_price"]
        #     )
        self.data.append(
            pd.Series([
                item["house_area"],
                item["house"],
                item["house_room"],
                item["total_price"],
                item["unit_price"]
            ], index=self.columns), name=item["house"]
        )
        # print(item)
        # print(insert_sql)
        # self.cu.execute(insert_sql)
        # self.con.commit()
        return item

    def close_spider(self, spider):
        # self.con.close()
        print(self.data.size)
