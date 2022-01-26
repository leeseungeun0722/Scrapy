import scrapy
from community.items import CommunityItem
from scrapy.http import Request, FormRequest

#게시판에 있는 제목 키워드 추충

KEYWORD = "이재명"

class BobaeSpider(scrapy.Spider):
    name = 'bobae'
    allowed_domains = ['https://security.bobaedream.co.kr/']
    
    def start_requests(self):
        for i in range(1,4): #페이지 정의 
            yield scrapy.Request("https://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={0}".format(i), self.parse)


    # 작성글 제목에 해당 키워드 있음 추출 
    def parse(self, response):
        items = []
        for i in range(0,30):   #페이지당 띄울 수 있는 작성글 수 
            item = CommunityItem()
            item['title'] = response.xpath('//*[@id="boardlist"]/tbody/tr/td[2]/a/text()')[i].extract()
            if(KEYWORD in item['title']):
                items.append(item)
        return items

    # def items_url(self, response):
    #     for 
           



    # def parse(self, response):
    #     item = CommunityItem()
    #     item["title"] = response.xpath('//*[@id="boardlist"]/tbody/tr/td[2]/a/text()').extract()
    #     yield item
        
    # def parse(self ,response):
    #     for i in range(0,30):
    #         title = response.xpath('//*[@id="boardlist"]/tbody/tr/td[2]/a/text()')[i].extract()
    #         yield title
   
    # def parse(self, response):
    #     item  
   
   
   
    # def parse(self, response):
