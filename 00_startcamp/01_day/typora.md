[TOC]



# h1 문서에 1개만

## h2

*이탤릭* 

**볼드**



## 1. 파이썬 기초

### 1.1 블라블라

### 1.2 블라블라

## 2. 파이썬 심화



아프니까 청춘이다.

> 아프면 병원가

```python
import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/marketindex/').text
# print(html)

# 2. 정보를 조작하기 편하게 바꾸고(정제)
soup = BeautifulSoup(html, 'html.parser')
# print(type(html))
# print(type(soup))

# 3. 바꾼 정보 중 원하는 것만 뽑아서
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

##exchangeList > li.on > a.head.jpy > div > span.value
# li.on 에서 on 뺄 것

# 4. 출력한다
print(exchange)
```

마크다운

# 외장 함수는 `import`로 가져와야한다.

[네이버](www.naver.com)

![]()

-  s

1. dddㅁㄴㅇㄹ
2. dddㅁㄴㅇㄹ
3. dddㅁㄴㅇㄹ