# 딕셔너리 만들기 - 1
lunch = {
    '중국집': '02-123-1234'
}

# 딕셔너리 만들기 - 2
dinner = dict(중국집='02', 일식집='031')

# 딕셔너리에 내용 추가하기
lunch['분식집'] =  '031-123-1234'
print(lunch)
# print(dinner)

# 딕셔너리 내용 가져오기
idol = {
    'bts': {
        '지민': 25,
        'RM': 24,
    }
}

# RM 의 나이는?
idol['exo']['RM']
idol.get('bts').get('RM')

# dict['key'] 로 존재하지 않는 key 를 접근할 경우 key error 가 발생하지만,
# dict.get('key') 으로 존재하지 않는 key를 접근할 경우 None 값을 출력한다.


