import webbrowser

# 1. 리스트가 필요
url = 'https://search.naver.com/search.naver?query='
idols = ['bts', 'nrg', 'hot', 'babyvox']


# 2. 반복문(for) 안에서 webborwser.open() 이 실행
for idol in idols:
    webbrowser.open_new(url + idol)