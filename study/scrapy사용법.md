## **scrapy 기사 긁어오기**

   [참고자료](https://l0o02.github.io/2018/06/19/python-scrapy-1/)

   <br/>

   scrapy 설치
   ```
   pip install Scrapy
   ```


1. scrapy 폴더 생성
   ```
   scrapy startproject (프로젝트 폴더 이름)
   ```  

2. 폴더 안으로 들어가서 tree 확인
   ```
   tree 폴더 이름
   ```
3. scrapy shell 들어가서 기사 tag 가져오기
   ```
   scrapy schell
   fetch('해당 기사 주소')
   response.xpath('가져올 html/text()').extract()
   ```
4. spider 파일 생성
   ```
   scrpay genspider 파일명 가져올주소
   ``` 
5. 이후 예시
   ```
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
    ```

6. setting 파일가서 csv로 변경 
   ```
   FEED_FORMAT = "csv"
   FEED_URL = "politics_news.csv"
   ```
7. 실행
   ```
   scrapy crawl (spider_name) -o (파일명).csv 
   ```



