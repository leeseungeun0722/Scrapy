import scrapy

from bobae.items import BobaeItem

# class BobaeSpider(scrapy.Spider):
#     name = "politic"
#     allowed_domains = ["www.bobaedream.co.kr/"]
#     start_urls = ["https://www.bobaedream.co.kr/list?code=politic"]

#     def parse(self, response):
#          for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
#             href = tr.xpath('./td[2]/a/@href')
#             url = response.urljoin(href[0].extract())
#             yield scrapy.Request(url, callback=self.parse_page_contents)

#     def parse_page_contents(self, response):
#         item = BobaeItem()
#         item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/span/text()')[0].extract()
#         yield item

# class RTSpider(scrapy.Spider):
#     name = "politic"
#     allowed_domains = ["www.bobaedream.co.kr/"]
#     start_urls = ["https://www.bobaedream.co.kr/list?code=politic"]

#     # def parse(self,response):
#     #     for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
#     #         href = tr.xpath('./td[2]/a/@href')
#     #         url = response.urljoin(href[0].extract())
#     #         yield scrapy.Request(url, callback=self.parse_page_contents)

#     def parse(self, response):
#         item = BobaeItem()
#         item["title"] = response.xpath('//*[@id="boardlist"]/tbody/tr/td[1]/text()').extract()
#         # item["genres"] = response.xpath('//*[@id="topSection"]/div[1]/score-board/p/text()')[0].extract()
#         yield item

class RTSpider(scrapy.Spider):
    name = "politic"
    allowed_domains = ["www.bobaedream.co.kr/"]
    start_urls = ["https://www.bobaedream.co.kr/view?code=politic&No=528169&bm=1"]

    # def parse(self,response):
    #     for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
    #         href = tr.xpath('./td[2]/a/@href')
    #         url = response.urljoin(href[0].extract())
    #         yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse(self, response):
        item = BobaeItem()
        item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()').extract()
        # item["genres"] = response.xpath('//*[@id="topSection"]/div[1]/score-board/p/text()')[0].extract()
        yield item