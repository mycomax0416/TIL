## 02_homework.md

1. mutable : list, set, dictionary

   immutable : string, tuple, range

2. ```python
   numbers_list = list(range(51))
   odd_numbers = numbers_list[1::2]
   print(odd_numbers)
   
   # a = list(range(1, 51))
   # b = a[0::2]
   # b
   ```

3. ```python
   student_dict = {
       '학생이름': 'Lee'
       '나이': 28
   }
   ```

## 02_workshop.md

1. ```python
   n = 5
   m = 9
   
   for i in range(m):
       for j in range(n):
           print('*', end='')
       print()
   ```

2. ```python
   sum(student.values()) / len(student)
   
   # 1.
   # student = {
   #     'python': 80, 
   #     'algorithm': 99, 
   #     'django': 89, 
   #     'flask': 83
   # }
   
   
   # result = 0
   # for score in student.values():
   #     result += score
   # print(result / len(student))
   
   # 2.
   # sum(student.values()) / len(student.keys())
   ```

3. ```python
   blood_types = ['A', 'B', 'C', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
   
   # 1.
   blood_dict = {}
   for blood in blood_types:
       if blood_dict.get(blood):
           blood_dict[blood] += 1
       else:
           blood_dict[blood] = 1
   print(blood_dict)
   
   # 2
   # blood_dict = {}
   # for blood in blood_types:
   #     blood_dict[blood] = blood_types.count(blood)
   # print(blood_dict)
   ```

4. 

