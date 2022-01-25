import scrapy
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from event_alarm.items import EventAlarmItem

class EventSpider(InitSpider):
    name = "event"
    allowed_domains = ["https://www.hanbit.co.kr"]
    login_page = "https://www.hanbit.co.kr/member/login.html"
    start_urls="https://www.hanbit.co.kr/myhanbit/myhanbit.html"

    def init_request(self):
        print("초기요구")
        return Request(url=self.login_page, callback=self.login)

    # def login(self, response):
    #     obj = {
    #         'retun_url':'https://www.hanbit.co.kr/index.html',
    #         'm_id':'tmddms7473',
    #         'm_passwd':'tmddms0722'
    #     }

    #     return FormRequest.from_response(response,
    #     method = 
    #     )