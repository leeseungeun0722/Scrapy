# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class CompanyItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()