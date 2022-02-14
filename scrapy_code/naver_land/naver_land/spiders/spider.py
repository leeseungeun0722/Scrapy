from urllib import response
from urllib.request import Request
import scrapy
import requests
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

seoul = 'https://new.land.naver.com/api/regions/list?cortarNo=1100000000'  # 1100000000 서울시 
seoul_List = literal_eval(requests.get(seoul,headers=headers).text)  # 서울시 APT를 text로 변환 시켜 dict로 저장

gangnum = 'https://new.land.naver.com/api/regions/list?cortarNo={}' 

# 읍 / 면 /동
regionKey = 'https://new.land.naver.com/api/regions/complexes?cortarNo={}' 

#아파트
apart = 'https://new.land.naver.com/api/complexes/overview/{}?complexNo={}'

detail = 'https://new.land.naver.com/api/complexes/{}/prices/real?complexNo={}&tradeType={}&year=5&priceChartChange=true&areaNo={}&type=table'

type = 'A1,B1,B2' #매매,전세,월세 주택유형ID 매매 3번째

type_split = type.split(',')



class SpiderSpider(scrapy.Spider):
    
    name = 'spider'
    allowed_domains = ['new.land.naver.com/']
    
    def start_requests(self):
            
            for i in seoul_List['regionList']:  #사울시 
                
                if i['cortarNo'] == '1168000000' : #시/군/구는 강남구로 한정시킨다.
                    
                    cortarNo = i['cortarNo']
                    gangnum_url = gangnum.format(cortarNo) #읍 면 동이 나올 url (개포동,청담동)   #https://new.land.naver.com/api/regions/list?cortarNo=1168011400
                    
                    yield scrapy.Request(gangnum_url, self.parse, dont_filter=True)


    def parse(self,response):
        items = []
        gangnum_List = literal_eval(response.text)

        for i in gangnum_List['regionList']:
            
            # dong_Num = i['cortarNo']
            
            if i['cortarNo'] == '1168011400': #개포로 한정
                dong_Num = i['cortarNo']
                dong_Name = i['cortarName']
                dong_url = regionKey.format(dong_Num) # 동 들이 나오는 url
                dong_List = literal_eval(requests.get(dong_url,headers=headers).text)

                for i in dong_List['complexList']: #https://new.land.naver.com/api/complexes/overview/119219?complexNo=119219
                
                    if i['realEstateTypeName'] == '아파트': #유형 형태에서 아파트만 추출

                            apartment_Num = i['complexNo'] #아파트 번호
                            apartment_Name = i['complexName']

                            apartment_url = apart.format(apartment_Num,apartment_Num)
                            apartment_List = literal_eval(requests.get(apartment_url,headers=headers).text)
                            
                            for i in apartment_List['pyeongs']:

                                pyeongNo = i['pyeongNo'] #타입번호
                                pyeongName = i['pyeongName'] #면적

                                for i in type_split:

                                    type_List = i # 매매 전세 월세                
                                    detail_url = detail.format(apartment_Num,apartment_Num,i,pyeongNo) #면적당 url뽑은거                                 
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
                                            # print(dong_Name,apartment_Num,apartment_Name,'매매 = ','타입 : ',detail_List['areaNo'],' 면적 : ',pyeongName, date,' 층수 : ',floor,' 가격 : ',price)
                                                # item['매매'] = dong_Name,dong_Num,apartment_Name,type_List,date,floor,price

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
                                                # item['전세'] = dong_Name,dong_Num,apartment_Name,apartment_Num,type_List,date,floor,price

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

                                                # price = i['leasePrice'],i['rentPrice']
                                                deposit = i['leasePrice']
                                                monthly = i['rentPrice']

                                                price = deposit,monthly
                    
                                                print(dong_Name,apartment_Num,apartment_Name,'월세 = ','타입 : ',detail_List['areaNo'],' 면적 : ',pyeongName, date,' 층수 : ',floor,price)
                                                # item['월세'] = dong_Name,dong_Num,apartment_Name,apartment_Num,type_List,date,floor,deposit,monthly

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
                                                # item['monthly'] = monthly

                                                items.append(item)
                                        
        return items                          
                    
            




      
                            
                            