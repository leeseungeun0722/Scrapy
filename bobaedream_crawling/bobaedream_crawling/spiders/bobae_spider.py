import scrapy

from bobaedream_crawling.items import BobaedreamCrawlingItem

PAGE = 3
KEYWORD = "이재명"

class BobaeSpiderSpider(scrapy.Spider):
    name = 'bobae'
    allowed_domains = ['www.bobaedream.co.kr']
    # start_urls = ['https://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page=1']

    def start_requests(self):
        for i in range(1,PAGE):
            main_url = "https://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={0}".format(i)
            yield scrapy.Request(main_url, self.parse)
 

    def parse(self, response):
        for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
            href = tr.xpath('./td[2]/a[1]/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url,callback=self.parse_page_contents)
                    

    def parse_page_contents(self, response):
        # items = []
        item = BobaedreamCrawlingItem()
        item["date"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/span/text()')[6].extract() #작성날짜
        item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract() #상세 제목
        item["contents"] =  response.xpath('//*[@id="print_area"]/div[2]/div/p/text()').extract()
        item["url"] =  response.xpath('//*[@id="copy"]/text()').extract() # 페이지 url
        # item["title"] = response.xpath('//*[@id="boardlist"]/tbody/tr/td[2]/a[1]/text()').extract()
        # item["url"] =  response.xpath('//*[@id="boardlist"]/tbody/tr/td[1]/text()').extract()
        # if('이재명' in item["title"]):
        #     items.append(item)
        # item["contents"] = item["contents"].replace( '\xa0',' ')
        yield item
    
