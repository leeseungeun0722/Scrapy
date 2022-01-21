# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Example2Item(scrapy.Item):
    title = scrapy.Field()
    data = scrapy.Field()
    contents = scrapy.Field()
    pass
