## 04_homework

1. 변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.

   - `L`ocal scope: 정의된 함수
   - `E`nclosed scope: 상위 함수
   - `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
   - `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

2. (1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. (X => return a, b 처럼 사용 가능)

   (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다. (O => 2개를 리턴하는 것처럼 보이지만 실제로는 튜플 1개가 리턴되는 것이다. 이는 하나의 튜플 객체입니다.)

   (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다. (O)

   (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다. (O)

3. 재귀함수를 쓰는 장점

   장점 : 직관적이고 이해하기 쉬운 경구가 많음(알고리즘에 경우)

   알고리즘적으로 가독성이 좋음. 변수 사용을 줄일 수 있음. 코드가 짧아짐.
   
   단점 : 작성하기 어려움. 메모리 스택이 넘치거나 프로그램이 느려지는 문제.
   
   함수를 불러오는 등 출력시간이 길어짐.

## 04_workshop

1. ```python
   # 1.
   def my_sqrt(n): # n = 2
       x, y = 1, n
       result = 1
       
       # 제곱근의 제곱(result**2)과 입력 값(n) 의 차이가 적어도 이 정도차이보다 작아지면!
       while abs(result**2 - n) > 1e-10:
           result = (x+y)/2 # 양쪽 끝 값을 더해서 2로 나눈다(절반을 구한다)
           # 위 근사치에 따라 x 또는 y 의 값을 바꾼다.
           if result**2 < n:
               x = result
           else:
               y = result
       return result
   
   # 2.
   import math
   
   def my_sqrt(n): # n = 2
       x, y = 1, n
       result = 1
       
       while not math.isclose(result**2, n):
           result = (x+y)/2 # 양쪽 끝 값을 더해서 2로 나눈다(절반을 구한다)
           # 위 근사치에 따라 x 또는 y 의 값을 바꾼다.
           if result**2 < n:
               x = result
           else:
               y = result
       return result
   ```

2. 

