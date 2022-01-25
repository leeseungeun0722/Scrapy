import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class ScrapySpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']
 
    def parse(self,response):
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        print(csrf_token)
        yield FormRequest.from_response(response,
         formdata={'csrf_token': csrf_token, 'username':'Coders', 'password': '12345'},
          callback=self.parse_after_login)
 
    def parse_after_login(self,response):
        print(response.xpath('.//div[@class = "col-md-4"]/p/a/text()'))





        import scrapy
from scrapy.http import FormRequest

class TodoSpider(scrapy.Spider):
    name = 'todologin'
    allowed_domains = ['https://www.hanbit.co.kr/']
    start_urls=['https://www.hanbit.co.kr/member/login.html']

    def parse(self,response):
        yield FormRequest.from_response(
            response,
            formdata={'m_id':'tmddms7473','m_passwd':'tmddms0722'},
            callback = self.parse_after_login
        )
    def parse_after_login(self,response):
        print(response)