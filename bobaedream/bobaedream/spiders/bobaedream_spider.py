import scrapy

from bobaedream.items import BobaedreamItem

#눈물의 보배드림 성공

class BobaedreamSpiderSpider(scrapy.Spider):
    name = 'bobaedream'
    allowed_domains = ['www.bobaedream.co.kr']
    start_urls = ['https://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page=1']
    # start_urls = ['https://www.bobaedream.co.kr/view?code=politic&No=528637&bm=1'] 
    # start_urls = ['https://www.bobaedream.co.kr/view?code=politic&No=525624&rtn=%2Flist%3Fcode%3Dpolitic']
    def parse(self,response):
        for i in range(8,20):
            for tr in response.xpath(f'//*[@id="boardlist"]/tbody/tr[{i}]'):
                 href = tr.xpath('./td[2]/a[1]/@href')
                 url = response.urljoin(href[0].extract())
                 print(url)
                 yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self,response):
        print("hello")
        item = BobaedreamItem()
        item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract() #상세 제목
        # item["title"] = response.xpath('//*[@id="boardlist"]/tbody/tr/td/a/text()').extract() #상세 제목
        yield item
       
