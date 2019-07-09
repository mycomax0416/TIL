import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/sise/').text
# print(html)

# 2. 정보를 조작하기 편하게 바꾸고(정제)
soup = BeautifulSoup(html, 'html.parser')
# print(type(html))
# print(type(soup))

# 3. 출력한다
kospi = soup.select_one('#KOSPI_now').text
print(kospi)