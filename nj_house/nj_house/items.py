# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NjHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house = scrapy.Field()
    house_area = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    house_room = scrapy.Field()

    pass
