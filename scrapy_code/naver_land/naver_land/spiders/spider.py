from urllib import response
from urllib import request
from urllib.request import Request
import scrapy
import requests
from scrapy import Request
from naver_land.items import NaverLandItem
from ast import literal_eval


headers = {
                'Accept': '*/*',
                'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDQzNzYxMjksImV4cCI6MTY0NDM4NjkyOX0.bhq4SOT956d8ap2J6Dd6vO1Ym8ZrR6MsYO1uAIeWlcE',
                'Accept-Encoding' : 'gzip, deflate, br',
                'Host': 'new.land.naver.com',
                'Referer' : 'https://new.land.naver.com/complexes/119219?ms=37.478448,127.0506355,17&a=APT:ABYG:JGC&e=RETAIL',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode' : 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }

MAIN_URL = 'https://new.land.naver.com/api/' #반복되는 MAIN URL

REGION_FIRST_KEY = '1100000000' #서울시

REGION_SECOND_KEY = '1168000000' #강남구

REGION_FIRST = f'https://new.land.naver.com/api/regions/list?cortarNo={REGION_FIRST_KEY}' #시군구 URL

REGION_FIRST_LIST = literal_eval(requests.get(REGION_FIRST, headers=headers).text)

REGION_SECOND = 'https://new.land.naver.com/api/regions/list?cortarNo={}' #읍면동 URL

DONG_APART = 'https://new.land.naver.com/api/regions/complexes?cortarNo={}' #동들의 아파트

APART = 'https://new.land.naver.com/api/complexes/overview/{}?complexNo={}'

DETAIL = 'https://new.land.naver.com/api/complexes/{}/prices/real?complexNo={}&tradeType={}&year=5&priceChartChange=true&areaNo={}&type=table'

type = 'A1,B1,B2' #매매,전세,월세 주택유형ID 매매 3번째

type_split = type.split(',')

class SpiderSpider(scrapy.Spider):
    
    name = 'spider'
    allowed_domains = ['new.land.naver.com/']
    
    def start_requests(self):
            
            for i in REGION_FIRST_LIST['regionList']:  
                
                if i['cortarNo'] == REGION_SECOND_KEY : 
                    
                    cortarNo = i['cortarNo']
                    REGION_SCOND_URL = REGION_SECOND.format(cortarNo) #읍 면 동이 나올 url (개포동,청담동) #https://new.land.naver.com/api/regions/list?cortarNo=1168011400
                    
                    yield scrapy.Request(REGION_SCOND_URL, self.parse, dont_filter=True)


    def parse(self,response):
        items = []
        REGION_SECOND_URL = literal_eval(response.text)

        print(response)

        for i in REGION_SECOND_URL['regionList']:
                dong_Num = i['cortarNo']
                dong_Name = i['cortarName']
                DONG_APART_URL = DONG_APART.format(dong_Num) # 동 들이 나오는 url
                dong_List = literal_eval(requests.get(DONG_APART_URL,headers=headers).text)

                for i in dong_List['complexList']: #https://new.land.naver.com/api/complexes/overview/119219?complexNo=119219
                
                    if i['realEstateTypeName'] == '아파트': #유형 형태에서 아파트만 추출

                            apartment_Num = i['complexNo'] #아파트 번호
                            apartment_Name = i['complexName'] #아파트 명

                            apartment_url = APART.format(apartment_Num,apartment_Num)
                            apartment_List = literal_eval(requests.get(apartment_url,headers=headers).text)
                            
                            for i in apartment_List['pyeongs']:

                                pyeongNo = i['pyeongNo'] #타입번호
                                pyeongName = i['pyeongName'] #면적

                                for i in type_split:

                                    type_List = i # 매매 전세 월세                
                                    detail_url = DETAIL.format(apartment_Num,apartment_Num,i,pyeongNo) #면적당 url뽑은거                                 
                                    detail_List = literal_eval(requests.get(detail_url,headers=headers).text)

                                    for i in detail_List['realPriceOnMonthList']:

                                        detail_type = i['realPriceList']

                                        for i in detail_type:
                                            item = NaverLandItem()

                                            year = i['tradeYear']
                                            month = i['tradeMonth']
                                            date = i['tradeDate']
                                            floor = i['floor']

                                            if type_List == 'A1': #매매

                                                price = i['dealPrice']

                                                item['dong_Name'] = dong_Name
                                                item['dong_Num'] = dong_Num
                                                
                                                item['apartment_Name'] = apartment_Name
                                                item['apartment_Num'] = apartment_Num
                            
                                                item['pyeongName'] = pyeongName

                                                item['type_List'] = '매매'
                                                item['year'] = year
                                                item['month'] = month
                                                item['date'] = date
                                                item['floor'] = floor
                                                item['price'] = price
                                                item['monthly'] = 'none'

                                                items.append(item)

                                            elif type_List == 'B1': #전세

                                                price = i['leasePrice']
                                                print(dong_Name,apartment_Num,apartment_Name,'전세 = ','타입 : ',detail_List['areaNo'],' 면적 : ',pyeongName, date,' 층수 : ',floor,' 가격 : ',price)
                                            
                                                item['dong_Name'] = dong_Name
                                                item['dong_Num'] = dong_Num
                                                
                                                item['apartment_Name'] = apartment_Name
                                                item['apartment_Num'] = apartment_Num
                            
                                                item['pyeongName'] = pyeongName

                                                item['type_List'] = '전세'
                                                item['year'] = year
                                                item['month'] = month
                                                item['date'] = date
                                                item['floor'] = floor
                                                item['price'] = price
                                                item['monthly'] = 'none'

                                                items.append(item)

                                            else : #월세

                                                deposit = i['leasePrice']
                                                monthly = i['rentPrice']

                                                price = deposit,monthly
                    
                                                print(dong_Name,apartment_Num,apartment_Name,'월세 = ','타입 : ',detail_List['areaNo'],' 면적 : ',pyeongName, date,' 층수 : ',floor,price)

                                                item['dong_Name'] = dong_Name
                                                item['dong_Num'] = dong_Num
                                                
                                                item['apartment_Name'] = apartment_Name
                                                item['apartment_Num'] = apartment_Num
                            
                                                item['pyeongName'] = pyeongName

                                                item['type_List'] = '월세'
                                                item['year'] = year
                                                item['month'] = month
                                                item['date'] = date
                                                item['floor'] = floor
                                                item['price'] = deposit
                                                item['monthly'] = monthly

                                                items.append(item)
                                        
        return items                          
                    
            




      
                            
                            