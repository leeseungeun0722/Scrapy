import scrapy

from all_community_crawl.items import AllCommunityCrawlItem

    
# 제목과 본문에 해당 키워드가 있으면 제목, 본문, 날짜, 기사url 추출
    
PAGE = 3
KEYWORD = input("키워드를 입력해주세요 (',' 로 구분 됩니다) :  ").split(',').re()
commuity_url = ["https://www.bobaedream.co.kr/list?code={0}"]
detail_url = ["&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={1}"]



class BobaeSpiderSpider(scrapy.Spider):
    name = 'bobae'
    allowed_domains = ['www.bobaedream.co.kr']
   
    #페이지 수
    def start_requests(self):
        for i in range(1,PAGE):
            main_url = "https://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={0}".format(i)
            yield scrapy.Request(main_url, self.parse)
 
    #페이지당 url
    def parse(self, response):
        for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
            href = tr.xpath('./td[2]/a[1]/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url,callback=self.parse_page_contents)
                    
    #해당 url 속 상세 기사 
    def parse_page_contents(self, response):
        items = []
        item = AllCommunityCrawlItem()
        item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract() #상세 제목 
        item["contents"] = response.xpath('//*[@id="print_area"]/div[2]/div/p/text()').re('(\w+)')
        if (KEYWORD in item["title"]) or (KEYWORD in item["contents"]) :  #제목이나 본문에 키워드 있음 추출
            item["date"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/span/text()')[6].re('(\w+)') #작성날짜
            item["url"] =  response.xpath('//*[@id="copy"]/text()').extract() # 페이지 url   
            item["enter"] = ('\n\n')
            items.append(item)
        return items



