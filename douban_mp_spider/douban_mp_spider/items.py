# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanMpSpiderItem(scrapy.Item):
    movie_name=scrapy.Field()
    star=scrapy.Field()
    comment=scrapy.Field()
    
	