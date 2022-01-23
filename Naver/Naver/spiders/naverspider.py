import scrapy
from Naver.items import NaverItem

MAX_PAGE = 20 # 데이터를 가져올 최대 페이지
LIST_COUNT = 20 # 한 페이지에 있는 책의 개수
class NaverSpider(scrapy.Spider):
    name="NaverSpider"
    allowed_domains=[
        "book.naver.com"
    ]
    start_urls=[
        f"https://book.naver.com/search/search.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&&page={i}" for i in range(1,MAX_PAGE+1) 
    ]
    # start_urls에 naver 책 페이지 1~21페이지까지 추가
    # XPath = //*[@id="searchBiblioList"]/li[i]/dl/dt/a for i in range(1,21)
    
    # 책들 리스트에서 각 책 정보 안으로 들어가는 링크 추출
    def parse(self,response):
        for i in range(1,LIST_COUNT):
            for tr in response.xpath(f'//*[@id="searchBiblioList"]/li[{i}]'):
                href = tr.xpath('dl/dt/a/@href')
                url = href[0].extract()
                # print(f"url : {url}")
                yield scrapy.Request(url=url,callback=self.parse_book_title)

    # 책 정보 링크 안으로 들어가 책 제목 추출
    # Xpath = //*[@id="container"]/div[4]/div[1]/h2/a/text()
    def parse_book_title(self,response):
        item = NaverBookItem()
        item['title'] = response.xpath('//*[@id="container"]/div[4]/div[1]/h2/a/text()')[0].extract().strip()
        print(f"item : {item}")
        yield item