# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommunityItem(scrapy.Item):
#   number = scrapy.Field() # 글번호
  title = scrapy.Field()  # 제목
  url = scrapy.Field()
#   date = scrapy.Field()   # 등록일
#   contents = scrapy.Field()  #본문 내용

