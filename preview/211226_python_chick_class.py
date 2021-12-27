### 파이썬 병아리반

names = ['쵸파', '루피', '상디', '조로']
names.append('해적왕')
for name in names:
    if len(name) > 2:
        print(name, '왔나요~?') #해적왕 왔나요~?



## 출력과 입력 그리고 변수
# print() 함수로 출력하기
print(34759**24341) #제곱
print('hello world') # hello world

# 변수
name = '최수민'
print(name)

a = 1024
print(a)

print(name+'님! 안녕하세요!') # 최수민님! 안녕하세요!
print(2021, name, '화이팅!') # 2021 최수민 화이팅!

# input() 함수로 문자열 값 입력받기
name = input() # 실행 후 이름 입력
print(name+'님! 안녕하세요!') # 최수민님! 안녕하세요!

name = input('이름을 넣어주세요: ') # 이름을 넣어주세요: 
print(name+'님! 안녕하세요!') # 최수민님! 안녕하세요!

age = input('나이를 입력해 주세요! : ') # 나이를 입력해 주세요! : 26
print(age-4) # TypeError: unsupported operand type(s) for -: 'str' and 'int'
print(int(age)-4) # 22(input으로 들어오는 값은 숫자처럼 보여도 str(문자열)로 받기 때문에 변수 age를 int(정수)로 바꾼다.)


## 연산자 사용하기
# 산술연산자
print(3 * 10) # 30 곱하기
print(3 ** 10) # 59049 제곱
print(3 % 10) # 3 나머지
print(3 / 2) # 1.5 나누기
print(3 // 2) # 1 몫

# 비교연산자
print(10 >= 3) # True
print(10 <= 3) # False
print(10 == 3) # False
print(10 != 3) # True
print(3 % 2 == 1) # True

# 논리연산자
print(1 == 1 and 2 != 1) # True
print(10 % 2 != 0 and 1 + 1 > 0) # False

print(10 < 5 or 10 == 5) # False
print(10 % 2 != 0 or 1 + 1 > 0) # True

print(not 10 > 5) # False
print(not 10 == 5) # True
print(not 0) # True
print(not 10) # False


## 함수 불러오기
import random
dice = random.randint(1, 6) # 1~6 사이의 랜덤숫자 1개를 뽑음
print(dice) # 2

import math
print(math.sqrt(2)) # 1.4142135623730951 제곱근(루트)


## 반복과 선택
# for 반복문
name = '최수민'
for i in name:
    print(i)

names = ['쵸파', '루피', '상디', '조로']
for name in names:
    print(name)

for i in [0, 1, 2, 3]:
    print(i ** 2)

for i in range(100): # range(100) -> [0 ~ 99], range(1, 100) -> [1 ~ 99], range(2, 100, 3) -> [2, 5, 8, 11 ~ 98] 3간격으로 생성
    print(i ** 2)

for i in range(100):
    print('나는 파이썬왕이 될 사람이다!!')

# if 조건문
if 10 > 0:
    print('안녕하세요?')

if 10 != 0 and 5 % 2 == 1:
    print('안녕하세요?')

passwd = int(input('비밀번호 4자리를 입력하세요 : '))
if passwd == 1531:
    print('비밀번호가 일치합니다.')

for i in range(10000):
    if i == 1531:
        print('비밀번호가 일치합니다.')

if passwd == 1531:
    print('비밀번호가 일치합니다.')
else:
    print('_______________________')

print('[ 소름끼치도록 놀라운 심리테스트 ]')
menu = input('당신이 좋아하는 음식을 입력해주세요 : ')
if menu == '짜장면':
    print('당신은 짜장면을 좋아하는 사람입니다.')
elif menu == '아이스크림':
    print('당신은 아이스크림을 좋아하는 사람입니다.')
elif menu =='사탕':
    print('당신은 사탕을 좋아하는 사람입니다.')
else:
    print('당신은 짜장면과 아이스크림과 사탕을 좋아하지 않는 사람입니다.')


## 순서 있는 저장 공간 리스트
# 리스트에 저장된 위치(index)로 값에 접근하기(indexing)
print(names[0]) # 쵸파
print(names[1]) # 루피
print(names[2]) # 상디
print(names[3]) # 조로

print(names[-1]) # 조로

# 리스트에 저장된 위치로 데이터의 일부 자르기(slicing)
print(names[0:2]) # ['쵸파', '루피']
print(names[1:3]) # ['루피', '상디']
print(names[1:]) # ['루피', '상디', '조로']
print(names[:]) # ['쵸파', '루피', '상디', '조로']

# 리스트에 값 추가하기
names.append('나미')
print(names) # ['쵸파', '루피', '상디', '조로', '나미']
 
print(len(names)) # 5
print(len('data analysis for everyone')) # 26

names = ['쵸파', '루피', '상디', '조로']
names.append('해적왕')
for name in names:
    if len(name) > 2:
        print(name, '왔나요~?') #해적왕 왔나요~?