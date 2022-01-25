import scrapy


class NaverbikePySpider(scrapy.Spider):
    name = 'naverbike'
    allowed_domains = ['https://auto.naver.com/bike/mainList.nhn']
    start_urls = ['http://auto.naver.com/bike/mainList.nhn']

    def parse(self, response):
        print(response.text)