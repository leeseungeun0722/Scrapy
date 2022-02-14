# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverLandItem(scrapy.Item):
    dong_Name = scrapy.Field()
    dong_Num = scrapy.Field()
    apartment_Name = scrapy.Field()
    apartment_Num = scrapy.Field()
    type_List = scrapy.Field()
    pyeongName = scrapy.Field()
    year =scrapy.Field()  
    month = scrapy.Field()  
    date = scrapy.Field()                                     
    floor = scrapy.Field()      
    price = scrapy.Field()          
    deposit = scrapy.Field()         
    monthly = scrapy.Field()
    

    