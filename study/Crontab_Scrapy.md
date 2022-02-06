# **Crontab 이용해서 특정시간에 자동 크롤링 하기**

<br/>


## **Crontab**

<br/>

>### **사용하는 이유?**
매일 혹은 장기적으로 실행해야 하는 예약작업이 있다면. 리눅스에 cron을 활용하여 작업을 수행할 수 있다.

나는 Crontab을 사용해 scrapy로 크롤링을 할 때 특정 시간에 자동으로 크롤링을 할 것이다.

<br/>

## **Crontab 사용법**

<br/>

>### **기본 에디터 설정**

```
select-editor
```

select-editor를 커맨트 창에 입력하면 기본 에디터를 설정이 나온다. 나는 주로 vi로 작업을 하기에 vi로 설정했다

>### **crontab 설정**
```
crontab -e
```

위에 명령어를 입력하면 crontab을 설정할 수 있는 장소가 나온다. vi를 쓴다면 i로 삽입을 하고 저장을 할땐 :wq를 입력하자

<br/>

## **주기설정**

<br/>

>### **크롤링할 주기 설정**
```
crontab -e
```
crontab 설정 장소에 들어가 맨 마지막 줄에 내가 실행하고 싶은 주기를 설정한다.

```
* * * * * 
```
나는 1분마다 실행하는 코드를 작성할 것이다. 다양한 시간 주기를 설정하고싶으면
[여기](https://velog.io/@jay2u8809/Crontab%ED%81%AC%EB%A1%A0%ED%83%AD-%EC%8B%9C%EA%B0%84-%EC%84%A4%EC%A0%95)
눌러서 참고하자

<br/>

>### **실행시킬 파일 설정**

<br/>

```
     * * * * *  [실행할 파일 위치] 
```



```
* * * * * bash /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh > /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh.log 2>&1
```

위에 명령문을 해석해보자면

**1분마다 spiders안에 있는 crawl.sh을 실행시켜 crawl.sh.log 파일에 기록하고 에러출력문을 백그라운드에서 표준출력문으로 기록한다.** 

<br/>

## **Scrapy 폴더 설정**

위에 실행 주기 설정한 코드를 보면 내가 실행할 scrapy 폴더에 crawl.sh라는 파일이 있다. 이는 직접 scrapy 폴더에 들어가서 추가해주자. (먼저 추가하고 해당 파일 경로를 복사한 뒤 위치 설정에 경로를 붙여넣자)

<br/>

>### **.sh 파일 설정 방법**
<br/>
실행시킬 crawl.sh 파일을 설정하는 방법을 알아보자.
원래 scrapy에 파일을 실행시킬 때 scrapy crawl (이름)을 사용했다. 이걸 그대로 .sh파일에 적용시키자

```
cd /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders

pipenv run scrapy crawl bobae -o ./spider.csv

```
먼저 spiders안에 있는 scrapy 파일을 실행시킬 경로를 적는다.

이후 pipenv run scrapy crawl [이름] -o ./[크롤링 저장시킬파일].csv 을 적으면 해당 파일로 가서 실행을 시킬 수 있다.

<br/>

## **실행**

<br/>

>### **crontab 실행시키기**
```
 sudo service cron start
```
crontab 설정과 scrapy파일 설정이 끝났으면 crontab을 실행시키자

<br/>

>### **crontab 중지**
```
 sudo service cron stop
```

>### **crontab 재실행**
```
 sudo service cron restart
```
<br/>


## **오류**

<br/>

>### **PATH 설정**
sudo service cron start으로 실행 시켰는데 command: not found 오류가 떴다. 이땐 crontab PATH 설정을 해줘야 된다

```
echo $PATH
```
위에 명령어로 환경변수들의 경로인 path를 출력해 복사한 뒤 
```
PATH=[복사한 경로]
```
crontab -e 로 crontab 설정 맨 윗 줄에 위에 처럼 경로를 설정하자

이후 다시 실행시키면 잘 실행이 된다🤗




<br/>

참고자료

[1](https://wikidocs.net/82568)
[2](https://jdm.kr/blog/2)



