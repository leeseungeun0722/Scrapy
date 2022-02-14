import scrapy
import time
import schedule
from bobae_commuity.items import BobaeCommuityItem

Keyword = ['윤석열']
# Keyword = input("(구분은 띄어쓰기로 합니다.) 키워드 입력해세요 : ").split(' ')
commuity_url = "https://www.bobaedream.co.kr/list?code={0}&page={1}"
commuity = ("best famous freeb ad politic nnews battle").split(' ')  #개별 커뮤니티
Page = 3 #페이지 설정

class BobaeSpiderSpider(scrapy.Spider):
    
    name = 'bobae'
    allowed_domains = ['www.bobaedream.co.kr']

    def start_requests(self):
        for i in commuity:  #커뮤니티별 url
            for j in range(1,Page):
                start_urls = commuity_url.format(i,j)
                yield scrapy.Request(start_urls, self.parse)

    #페이지당 url
    def parse(self, response):
        for tr in response.xpath('//*[@id="boardlist"]/tbody/tr'):
            href = tr.xpath('./td[2]/a[1]/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url,callback=self.parse_page_contents)
                    
    #해당 url 속 상세 기사 
    def parse_page_contents(self, response):
        items = []
        item = BobaeCommuityItem()
        title = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract() 
        contents = response.xpath('//*[@id="print_area"]/div[2]/div/p/text()').re('(\w+)') 

        for i in Keyword: #키워드 리스트에서 하나씩 해당 키워드가 있는 글 추출
            if ( i in title or i in contents) :  #제목이나 본문에 키워드 있음 추출
                item["title"] = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract() #상세 제목 
                item["url"] =  response.xpath('//*[@id="copy"]/text()').extract() # 페이지 url   
                items.append(item)
        return items


    def start_crawl():
        print('scrapy crawl bobae')
    
    start_crawl()

## 추가 하고 싶은 거 => 각 커뮤니티 당 몇 페이지 까지 있는지 추출



