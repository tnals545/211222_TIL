# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.
from audioop import avg


print("Hello World") # 정답

# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's consmetics") # 정답

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
print('신씨가 소리질렀다. "도둑이야".') # 정답

# 004 print 기초
# 화면에 "C:\Windows"를 출력하세요.
print("\"C:\Windows\"") # "" 이것도 출력되야 하는줄..   출력값 : "C:\Windows"
# 해설 : print("C:\Windows")    출력값 : C:\Windows

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.") # \n은 줄바꿈, \t는 탭? 인거같다.
# 해설 : \t는 탭을 의미하고 \n'은 줄바꿈을 의미합니다.

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일") # 오늘은 일요일
# 해설 : 여러 값을 출력하려면 print 함수에서 쉼표로 구분해주면 됩니다. 따라서 오늘은 다음에 공백이 하나 있고 일요일이 출력됩니다.

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print('naver;'+'kakao;'+'sk;'+'samsung')
# 해설 : print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.
# print("naver", "kakao", "samsung", sep=";")

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print('naver', 'kakao', 'sk', 'samsung', sep='/')
# 해설 : print("naver", "kakao", "samsung", sep="/")

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first", end=" ");print("second") # first second
# 해설 : print("first", end=""); print("second") # firstsecond

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.
print(5/3) # 1.6666666666666667
# 해설 : 출력하고 싶은 값을 print 함수의 인자로 적어주면 됩니다.
# print(5/3)

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung = 50000
print(samsung * 10) # 500000
# 해설
# 삼성전자 = 50000
# 총평가금액 = 삼성전자 * 10
# print(총평가금액)

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
market_cap = 298000000000000
current_price = 50000
per = 15.79
print(market_cap)
print(current_price)
print(per)
# 해설
# 시가총액 = 298000000000000
# 현재가 = 5000
# PER = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# hello! python
print(s+'!', t) # hello! python
# 해설
# print(s+"!", t)

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 
# 내 예상 : 8, 사칙연산은 곱셈과 나눗셈 후 덧셈 뺄샘이기 때문임
# 해설 : 8

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# >> a = "132"
# 예상 : <class 'str'>
# 해설
# a = "132"
# print(type(a))
# <class 'str'>

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
# num_str = "720"
print(int(num_str))
# 해설
# num_str = "720"  #형변환
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100
print(str(num))
# 해설
# num = 100
# result = str(num)
# print(result, type(result))

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
a = "15.79"
print(float(a))
# 해설
# data = "15.79"
# data = float(data)
# print(data, type(data))

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2021"
year_int = int(year)
print(year_int - 2, year_int - 1, year_int)
# 해설
# year = "2020"
# print(int(year)-3)  # 2017
# print(int(year)-2)  # 2018
# print(int(year)-1)  # 2019

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
price = 48584 * 36
print(price) # 1,749,024
# 해설
# 월 = 48584
# 총금액 = 월 * 36
# print(총금액)

# 021 문자열 인덱싱
# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0], letters[2])
# 해설
# 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.
# lang = 'python'
# print(lang[0], lang[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
license_plate.split(' ')[1]
# 해설
# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4])
# 해설
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
# print(string[::2])

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1]) # NOHTYP
# 해설
# print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' ')) # 010 1111 2222
# 해설
# phone_number1 = phone_number.replace("-", " ")
# print(phone_number1)

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', '')) # 01011112222
# 해설
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace('-', '')
# print(phone_number1)

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
print(url.split('.')[1]) # kr
# 해설
# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
lang[0] = 'P'
print(lang)
# 내 예상 : Python
# 해설
# 문자열은 수정할 수 없습니다.
# 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string_A = string.replace('a', 'A')
print(string_A) # Abcdfe2A354A32A
# 해설
# string = 'abcdfe2a354a32a'
# string = string.replace('a', 'A')
# print(string)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
# 내 예상 : 'abcd' >> 실행된 결과를 변수에 넣어두지 않았기 때문에 원본은 그대로다.
# 해설
# abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다.
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
>> a = "3"
>> b = "4"
>> print(a + b) # "34"
# 해설
# 두 문자열에 대해 덧셈 기호는 문자열의 연결을 의미합니다. 따라서 "34"라는 새로운 문자열이 생성되고 그 값이 print 함수에 의해 화면에 출력됩니다.

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
>> print("Hi" * 3) # "HiHiHi"
# 해설
# 문자열에 대한 곱셈은 문자열의 반복을 의미합니다. 따라서 다음과 같이 문자열이 출력됩니다.
# HiHiHi

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
print('-' * 80) # --------------------------------------------------------------------------------
# 해설
# print("-" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
>>> t1 = 'python '
>>> t2 = 'java '
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# python java python java python java python java
print((t1 + t2) * 4) # 변수에 들어간 value값에 space 넣어서 해결
# 해설
# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
print('이름: %s 나이 : %d' % (name1, age1))
print('이름: %s 나이 : %d' % (name2, age2))
# 해설
# print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미합니다.

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
format1 = ('이름 : {} 나이 : {}').format(name1, age1)
print(format1)
format2 = ('이름 : {} 나이 : {}').format(name2, age2)
print(format2)
# 해설
# 문자열의 포맷 메서드는 타입과 상관없이 값이 출력될 위치에 { }를 적어주면 됩니다.
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.

# f-string 용어는 처음봐서 몰랐는데 해설 보니까 쓴적은 있음.

# 해설
# f-string은 문자열 앞에 f가 붙은 형태입니다.
# f-string을 사용하면 {변수}와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력할 수 있습니다.
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
rep = int(상장주식수.replace(',', ''))
print(rep)
type(rep)
# 해설
# 정수형으로 타입을 변환하려면 int( ) 함수를 사용하면 됩니다.
# 이때 숫자 형태의 문자열에 컴마가 있는 경우 바로 변환된지 않습니다.
# 먼저 문자열의 replace 메서드로 컴마를 제거한 후 변환해야합니다.
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 해설
# 문자열에서 슬라이싱을 사용하면 여러 글자를 접근할 수 있습니다.
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())
# 해설
# 문자열에서 strip( ) 메서드를 사용하면 좌우의 공백을 제거할 수 있습니다.
# 이때 원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환됩니다.
# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)

# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"

ticker.upper()

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"

ticker.lower()

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
a = 'hello'
a.capitalize()

# 044 endswith 메서드
file_name = "보고서.xlsx"

file_name.endswith(('xlsx', 'xls'))

# 045 endswith 메서드
file_name = "보고서.xlsx"

file_name.endswith(('xlsx', 'xls'))
# True

# 046 startswith 메서드
file_name = "2020_보고서.xlsx"

file_name.startswith('2020')

# 047 split 메서드
a = "hello world"

a.split(' ')

# 048 split 메서드
ticker = "btc_krw"

ticker.split('_')

# 049 split 메서드
date = "2020-05-01"

date.split('-')

# 050 rstrip 메서드
data = "039490     "

data.rstrip()

# 051 리스트 생성
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 052 리스트에 원소 추가
movie_rank = movie_rank + ['배트맨']

# 053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 054
del movie_rank[3]
print(movie_rank)

# 055
del movie_rank[2:]
print(movie_rank)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 57
nums = [1, 2, 3, 4, 5, 6, 7]
min(nums)
max(nums)

# 58
nums = [1, 2, 3, 4, 5]
sum(nums)

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두",
        "쫄면", "소시지", "라면", "팥빙수", "김치전"]

len(cook)

# 60
nums = [1, 2, 3, 4, 5]

np.mean(nums)