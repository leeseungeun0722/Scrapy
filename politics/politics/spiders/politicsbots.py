import scrapy

class PoliticsbotsSpider(scrapy.Spider):
    name = 'politicsbots'
    start_urls = ['https://www.joongang.co.kr/politics']

    def parse(self, response):
        titles =  response.xpath('//*[@id="story_list"]/li/div[2]/h2/a/text()').extract()    
        previews = response.xpath('//*[@id="story_list"]/li/div[2]/p/a/text()').extract()          
        dates = response.xpath('//*[@id="story_list"]/li/div[2]/div/p/text()').extract()           

        for item in zip(titles, previews, dates):
            scraped_info = {
                'title' : item[0].strip(),
                'preview' : item[1].strip(),
                'date' : item[2].strip(),
            }
            yield scraped_info
