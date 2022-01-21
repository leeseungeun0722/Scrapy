import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
             'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').get()
        print(f'URL is: {url}')
        print(f'Title is: {title}')