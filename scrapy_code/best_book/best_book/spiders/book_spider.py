import scrapy

from best_book.items  import BestBookItem

class BookSpider(scrapy.Spider):
    name = "bestbook"
    allowed_domains = ["aladin.co.kr"] 
    start_urls = ["https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=170"]

    #50권의 베스트 샐러 책 세부정보 링크 추출
    def parse(self,response):
        for i in range(2,51):
             for div in response.xpath(f'//*[@id="Myform"]/div[{i}]'):
                 href = div.xpath('./table/tr/td[3]/table/tr[1]/td[1]/div[1]/ul/li/a/@href')
                 url = href[0].extract()
                 #  print(f"url : {url}")
                 print(url)
                 yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self,response):
        # item = BestBookItem()
        # item["title"] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[2]/div/a[1]/text()')[0].extract()
        # item["author"] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[3]/a[1]/text()')[0].extract().strip()
        # item["price"] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[4]/div[4]/div/div[3]/ul/li[1]/div[2]/text()')[0].extract()
        # item["score"] = response.xpath('//*[@id="wa_product_top1_wa_Top_Ranking_pnlRanking"]/div[2]/a[2]/text()')[0].extract()
        # yield item
        print("hello")
        