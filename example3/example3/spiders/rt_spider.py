import scrapy

from example3.items import Example3Item

class Rt_spiderSpider(scrapy.Spider):
    name = "RottenTomatoes"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/top/bestofrt/?year=2017"]

    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath('./td[3]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

        def parse_page_contents(self, response):
            item = Example3Item()
            item["title"] = response.xpath('//*[@id="topSection"]/div[1]/score-board/h1/text()')[0].extract().strip()
            item["genres"] = response.xpath('//*[@id="topSection"]/div[1]/score-board/p/text()')[0].extract() 
            yield item

    
    
