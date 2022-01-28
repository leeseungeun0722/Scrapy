import scrapy
from bobaedream_crawler.items import BobaedreamCrawlerItem


LIST = 30 # 한 페이지에 있는 게시글 수
SEARCH = input("단어들 입력 (단어는 공백으로 구분) >> ").split() # 검색할 단어들 입력 (단어들 중 하나라도 있으면 파일에 추가)
ORIGINAL_URL = 'https://www.bobaedream.co.kr/list?code={}' # 기본이 되는 URL
CATE_LIST = 'best famous freeb ad politic battle strange girl accident music national army import truck hotcar skybr dica vi special wheel  bbstory nnews'.split() # 카테고리

used_url = []

class BobaedreamSpider(scrapy.Spider):
    
    name = 'BobaedreamSpider'

    start_urls = []

    for cate in CATE_LIST:

        start_urls.append(ORIGINAL_URL.format(cate))
    
    # print(start_urls)

    
    def parse(self,response): # 페이지 처리하는 함수

        get_max = response.url.split('=')
        
        MAX_PAGE = int(get_max[-1])
        

        if '다음' in response.css('img::attr(alt)').getall(): # 다음이 있다는것은 10페이지가 무조건 존재한다는 것

            for page in range(MAX_PAGE,MAX_PAGE+11):

                url = response.url.split('=')

                url[-1] = str(page)

                url = '='.join(url)

                if url not in self.start_urls:

                    self.start_urls.append(url)


        else: # 존재하지 않는다면 몇페이지는 존재 할 수 있음 (예시 : 6081~6088 -> 다음 없음)

            pagenum = response.xpath('//*[@id="Content"]/div[2]/div[2]/form/div[1]/ul')[0].extract() 

            number = pagenum.css('li > a > span::text').getall()

            max_number = int(number[-1])

            for page in range(MAX_PAGE,max_number+1):

                url = response.url.split('=')

                url[-1] = str(page)

                url = '='.join(url)

                if url not in self.start_urls:

                    self.start_urls.append(url)

        for url in self.start_urls:

            yield scrapy.Request(url = url, callback = self.get_url)


    def get_url(self,response): # 각 게시물로 들어가는 url을 추출하는 함수

        back_urls = response.xpath('//*[@class="pl14"]').css('a::attr(href)').getall()

        urls = []

        for url in back_urls:

            if 'javascript' in url: # a href에 javascript가 포함된 경우 추출하지 않음

                continue

            urls.append('https://www.bobaedream.co.kr/' + url)
        

        for url in urls:

            try:

                yield scrapy.Request(url = url, callback = self.get_article)

            except: # 만약 해당 url에 접근할 수 없다면 예외 처리

                print("예외 발생")

                break
    

    def get_article(self,response):

        # 글 본문 추출
        articles = response.xpath('//*[@id="print_area"]/div[2]/div').css('p::text').getall()

        # 글 제목 추출
        title = response.xpath('//*[@id="print_area"]/div[1]/dl/dt/strong/text()')[0].extract()

        for search in SEARCH:

            for article in articles:

                if search in article or search in title:

                    item = BobaedreamCrawlerItem()

                    item['_0title'] = title
                    
                    item['_1url'] = response.url

                    if item['_1url'] not in used_url:
                        
                        # 만약 이미 추출했던 url이면 더이상 추출하지 않음
                        used_url.append(item['_1url'])

                        print(item)

                        yield item

                else:

                    continue