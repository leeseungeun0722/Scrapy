# **Crontab 기본**

<br/>


## **Crontab 기본**

<br/>

>### **crontab -e**
편집할 수 있는 곳이 로딩이 되며 크론탭을 설정할 수 있는 장소이다
이곳에 크론탭 명렁어 입력후 저장하자

<br/>

>### **crontab -l**
cat 명령어로 파일을 읽은 것 처럼 표출 출력으로 크론탭 내용이 나오게 된다

<br/>

## **Crontab 주기설정**

<br/>

>###  * &nbsp; &nbsp; &nbsp;* &nbsp; &nbsp;&nbsp; *&nbsp; &nbsp;&nbsp; &nbsp; * &nbsp; &nbsp;&nbsp; * 
>분&nbsp; &nbsp;시간&nbsp;&nbsp;&nbsp; 일&nbsp;&nbsp; 월&nbsp;&nbsp; 요일

<br/>

>### **매분실행** ###
```
* * * * * bash /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh
```

***** 뒤에는 실핼시킬 파일 경로를 입력하자

=> **일분마다 crawl.sh파일을 실행**


다양한 시간 설정은 [여기](https://velog.io/@jay2u8809/Crontab%ED%81%AC%EB%A1%A0%ED%83%AD-%EC%8B%9C%EA%B0%84-%EC%84%A4%EC%A0%95)를 참고하자

<br/>

## **크론 로깅**

크론탭을 사용해서 해당 처리 내역에 대해 로그를 남기고 싶을 때 다음과 같이 써보자

```
* * * * * bash /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh > /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh.log 2>&1
```

위에 처럼 작성하면 매분마다 crawl.sh.log 파일이 갱신되어 작업 내용이 어떻게 처리 되었는지 알 수 있다 2>&1을 제거하면 쉘스크립트에서 표준 출력 내용만 나온다

<br/>

## **리눅스 특수문자 정리**


<br/>

>### **표준 출력** ###

```
ls > text.txt
```
[표준 출력을 파일에 기록한다] 표준 출력을 뜻하는 특수문자는 '>'이다 .

=> **ls에 출력된 내용을 text.txt에 기록한다** 

```
ls >> text.txt
```
[표준 출력을 파일 끝에 덧붙인다] 그 외에도 표준 출력을 두번 연속으로 사용하게 되면 다음 처럼 시용한다

=> **ls에 출력된 내용을 text.txt에 덧붙여 기록한다.** 

<br/>

>### **명령 문자** ###


<br/>

```
; (명령의 끝을 나타낸다)
|| (이전의 명렁이 실패하면 실행하는 조건문 문자)
&& (이전의 명령이 성공하면 실행하는 조건문 문자)
& (명령을 백그라운드에서 실행한다)
$ (변수에 접근할 수 있는 문자)
```

>### **변수 접근 기호** ###


<br/>

```
0 (표준 입력)
1 (표준 출력)
2 (에러 출력)
```

위 같은 명령 문자와 변수 접근 기호를 합치면 &1, &2와 같은 명령도 가능하다 

```
* * * * * bash /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh > /home/seungeun/scrapy_test/scrapy/bobae_commuity/bobae_commuity/spiders/crawl.sh.log 2>&1
```
=> 1분마다 crawl.sh을 실행시켜 crawl.sh.log 파일에 기록하고 에러출력문을 백그라운드에서 표준출력문으로 기록한다. 



<br/><br/>

[참고자료](https://jdm.kr/blog/4)

