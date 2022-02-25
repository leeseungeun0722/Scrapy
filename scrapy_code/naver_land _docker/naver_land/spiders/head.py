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

URL = MAIN_URL + 'regions/{}?cortarNo={}' #동들의 아파트

APART = MAIN_URL + 'complexes/overview/{}?complexNo={}'

DETAIL = MAIN_URL + 'complexes/{}/prices/real?complexNo={}&tradeType={}&year=5&priceChartChange=true&areaNo={}&type=table'

TYPE = ['A1','B1','B2']