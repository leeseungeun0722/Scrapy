import scrapy

import story_list

from scrapy.spiders import spider

from Company.Items import CompanyItem

from scrapy.http import requests

from scrapy.selector import selector
reload(sys)
sys.setdefaultencoding('utf-8')

class company_spider(scrapy.spider):
    name = "companyspider"
    allowed_domains = ["https://www.jobkorea.co.kr/"]

    def start_requests(self):
        for i in range(1,5,1):
            yield scrapy.requests("https://www.jobkorea.co.kr/starter/?chkSubmit=1&schCareer=1&schLocal=&schPart=10016&schMajor=&schEduLevel=&schWork=2&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=")

    def parse(self, response):
        for colum in response.xpath('//div[@class="filterListArea"]/ul/li/text()').extract()
            item = CompanyItem()
            item['company'] = colum.xpath('//*[@id="devStarterForm"]/div[2]/ul/li/div[1]/div[1]/a/text()').extract()   
            item['title'] =  colum.xpath('//*[@id="devStarterForm"]/div[2]/ul/li/div[2]/div[1]/a/span/text()').extract()
            yield item     