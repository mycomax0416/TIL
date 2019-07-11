from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'


@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    <ol></ol>

    """
# variable routing (변수 라우팅)
@app.route('/greeting/<name>')
# @app.route('/greeting/<string:name>') -> 위에것과 똑같음(string은 기본값이라 생략 가능)
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name = name)

@app.route('/cube/<int:number>')
def cube(number):
    # return f'{number} 세제곱은 {number**3}입니다.'
    answer = number ** 3
    return render_template('cube.html', html_number = number, html_answer = answer)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu_list = ['볶음밥', '카레', '치킨', '햄버거']
    order = random.sample(menu_list, people)
    return str(order)

    # menu = random.choice(menu_list)
    # return f'메뉴는 {menu} {people}인 분 입니다.'


# @app.route('/lunch/<int:people>')
# def lunch(people):
#     menu = ['짜장면', '짬뽕', '탕수육', '팔보채', '마파두부밥', '북경오리']
#     order = random.sample(menu, people)
#     return str(order)

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '알라딘', '기생충']
    return render_template('moive.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html') 
 
@app.route('/pong')
def pong():
    # print(request.args)
    name = request.args.get('data') # ping 박스
    return render_template('pong.html', name = name)

@app.route('/naver')
def naver():
    return render_template('naver.html')

# https://search.naver.com/search.naver?query=

@app.route('/google')
def google():
    return render_template('google.html')

# https://www.google.com/search?q=

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/result')
def result():
    results = ['잘생김', '못생김', '귀여움', '역겨움', '잘난척', '쑥쓰러움', '애교', '성욕', '돈복', '허세']
    picks = random.sample(results, 3)
    name = request.args.get('username')
    return render_template('result.html', name=name, picks=picks)