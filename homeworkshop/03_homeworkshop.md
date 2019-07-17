## 03_homework

1. ```python
   dir(__builtins__) # 명령어
   # ex)
   str()
   int()
   print()
   max()
   min()
   ```

2. ```python
   def ssafy(name, location='서울'):
       print(f'{name}의 지역은 {location}입니다.')
   
   # 1.
   ssafy(location='대전', name='철수')
   # 2. 
   ssafy('길동', location='광주')
   # 3. 오류코드
   ssafy(name='허준', '구미')
   ```

3. ```python
   def my_func(a,b):
       c = a + b
       print( c )
       
   result = my_func(4,7)
   print(result) # -> None : 키워드 인자 활용한 뒤에 위치 인자를 사용할 수 없다.
   ```

## 03_workshop

```python
# 짝수 - NAAN
# 홀수 - S/AS

def is_palindrome(word): # NAAN
    list_word = list(word) # ['N', 'A', 'A', 'N']
    # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word) // 2): # 2
        if list_word[i] != list_word[-i-1]:
            return False
        return True
    
    word == word[::-1] # pythonic !!!
```

