import scrapy

from bobaecrawl.items import BobaecrawlItem

class BobaeSpider(scrapy.Spider):
    name = "bobaebae"
    allowed_domains = ["www.bobaedream.co.kr/"]
    start_urls = ["https://www.bobaedream.co.kr/list?code=politic"]

    def parse(self, response):
        for i in range(1,10):
            for tr in response.xpath(f'//*[@id="boardlist"]/tbody/tr[{i}]'):
                href = tr.xpath('./td[2]/a/@href')
                url = href[0].extract()
                #print(f"url : {url}")
                yield scrapy.Request(url = url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        item = BobaecrawlItem()
        item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract()
        yield item
