import scrapy
from example2.item import Example2Item

class ExampleSpider(scrapy.Spider):
    name = 'examplespider'

    def start_requests(self):
        urls = [
            'https://www.82cook.com/entiz/read.php?bn=15&num=1504525'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        