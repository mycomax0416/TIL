# import webbrowser

# 1. 리스트가 필요
# sites = ['www.google.com', 'www.naver.com', 'www.daum.net']
# idols = ['bts', 'nrg', 'hot', 'babyvox']
# url = 'https://search.naver.com/search.naver?query='
#webbrowser.open('www.google.com')

# 2. 반복문(for) 안에서 webborwser.open() 이 실행
# for site in sites:
    # webbrowser.open_new(url)
# for idol in idols:
    # webbrowser.open_new(url + idol)


import requests

response = requests.get('https://www.naver.com/').status_code
print(response)