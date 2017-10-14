# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SexTextItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#定义一个色情小说的类
class Blue_book(scrapy.Item):
    title = scrapy.Field()#文章标题
    content = scrapy.Field()#文章正文
    the_url = scrapy.Field()#文章url
    the_url_id = scrapy.Field()#用md5缩短url长度以节省资源