import scrapy

class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    start_urls = ['http://corners.gmarket.co.kr/BestSellers']

    def parse(self, response):
        title = response.
