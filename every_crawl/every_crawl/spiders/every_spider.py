import scrapy
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from every_crawl.items import EveryCrawlItem

class EverySpider(InitSpider):
    name = "everytime"
    allowed_domains = ["https://everytime.kr/"]
    login_page = "https://everytime.kr/login"
    start_urls = "https://everytime.kr/369476"

    def init_request(self):
        print("=============[init_request]=============")
        yield Request(url=self.login_page, callback=self.login)

    def login(self, response):
        return FormRequest.from_response(
            method="GET",
            response = response,
            formdata= { 'userid': 'tmddms1201', 'password': 'tmddms0722@'},
            callback=self.check_login_response
        )
    def check_login_response(self,response):
        print("=============[확인중]=============")
        print(response)

        # if response ==:
        #     print("로그인 실패")

        # else:
        #     print("로그인 성공")

    def parse(self,response):
        print('parse')

