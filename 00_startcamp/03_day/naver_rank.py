
# 요청 보내서 html 파일 받고

# 뷰숲으로 정제

# select 메서드로 사용해서 list 를 얻어낸다

# 뽑은 list 를 with 구문으로 잘 작성해보자.(txt)

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
with open('naver_rank.txt', 'w') as f:
    searchs = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
    for search in searchs:
        f.write(f'{search.text}\n')

#with open('example.txt', 'w', encoding='utf-8') as f:

# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.naver.com'
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html.parser')
# searchings = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')
# with open('naver_search.txt', 'w', encoding='utf-8') as f:
#     for searching in searchings:
#         rank = searching.select_one('span.ah_r').text
#         keyword = searching.select_one('span.ah_k').text
#         f.write(f'{rank}위: {keyword}\n')