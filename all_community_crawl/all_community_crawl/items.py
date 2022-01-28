# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AllCommunityCrawlItem(scrapy.Item):
    title = scrapy.Fleid()
    date = scrapy.Fleid()
    url = scrapy.Fleid()
    contents = scrapy.Fleid()

