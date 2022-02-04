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

>### **위치 설정**

     * * * * *  [현재위치] [실행할 파일 위치] > [실행된 결과 값 저장할 곳]


아직 저렇게 실행 되는 이유를 잘 몰라서 찾아봐야된다.  

```
* * * * * bash /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh > /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh.log 2>&1
```
crontab 설정에 위에 실행주기와 파일 경로를 저장한다.

<br/>

## **Scrapy 폴더 설정**

위에 실행 주기 설정한 코드를 보면 내가 실행할 scrapy 폴더에 crawl.sh라는 파일이 있다. 이는 직접 scrapy 폴더에 들어가서 추가해주자. (먼저 추가하고 해당 파일 경로를 복사한 뒤 위치 설정에 경로를 붙여널자)






