# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class BobaedreamCrawlerItem(Item):

    _0title = Field() # 글 제목

    _1url = Field() # 글 url 
