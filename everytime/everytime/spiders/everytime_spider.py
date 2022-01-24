from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from everytime.items import EverytimeItem

class EverySpider(InitSpider):
    name = "everything"
    login_page = "https://everytime.kr/login"
    start_urls = "https://everytime.kr/"

    def init_request(self):
        print("================[초기실행]================")
        return Request(url = self.login_page, callback = self.login)

    def login(self, response):
        return FormRequest.from_response(
            response,
            method = "POST",
            formdata={
                'userid':'tmddms1',
                'password':'tmddms22@'
            },
            callback=self.check_login_response
        )

    def check_login_response(self, response):
        print("================[확인중]================")

        if response == '200 https://everytime.kr/login' :
            print("로그인 실패")
        else :
            print("로그인 성공")