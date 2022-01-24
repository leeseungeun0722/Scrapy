import scrapy
from company.items import CompanyItem

class company_spider(scrapy.Spider):
    name = "company"
    allowed_domains = ["www.jobkorea.co.kr/"]

    def parse(self):
        for i in range(1,5,1):
            yield scrapy.Request("http://www.jobkorea.co.kr/starter/?schPart=10016&Page={0}".format(i),callback = self.parse_page)

    def parse_page(self,response):
        Item = CompanyItem()
        Item['title'] = response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li/div[2]/div[1]/a/span/text()').extract()
        Item['company']= response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li/div[1]/div[1]/a/text()').extract()
        yield item 