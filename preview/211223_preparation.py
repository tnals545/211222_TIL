# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.
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