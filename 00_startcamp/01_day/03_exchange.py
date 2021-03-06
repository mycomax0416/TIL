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
# 위의 엔화는 달러와는 다르게 li.on 에서 on 뺄 것

# 4. 출력한다
print(exchange)