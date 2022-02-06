# 모듈

### 모듈 만들기
# mod1.py
# def add(a, b):
#     return a + b

# def sub(a, b): 
#     return a-b

### 모듈 불러오기
import mod1
print(mod1.add(3, 4)) # 7
print(mod1.sub(4, 2)) # 2

from mod1 import add
add(3, 4) # 7

from mod1 import add, sub
from mod1 import *

### if __name__ == "__main__": 의 의미
# mod1.py 파일 수정
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# print(add(1, 4))
# print(sub(4, 2))


# C:\Users\pahkey> cd C:\doit
# C:\doit> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod1
# 5
# 2

# 엉뚱하게도 import mod1을 수행하는 순간 mod1.py가 실행이 되어 결괏값을 출력한다. 우리는 단지 mod1.py 파일의 add와 sub 함수만 사용하려고 했는데 말이다.
# 이러한 문제를 방지하려면 mod1.py 파일을 다음처럼 변경해야 한다.

# mod1.py 
# def add(a, b): 
#     return a+b

# def sub(a, b): 
#     return a-b

# if __name__ == "__main__":
#     print(add(1, 4))
#     print(sub(4, 2))

# if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.

# 위와 같이 수정한 후 다시 대화형 인터프리터를 열고 실행해 보자.

# >>> import mod1
# >>>

# 아무 결괏값도 출력되지 않는 것을 확인할 수 있다.

# *(__name__ 변수란?)*

# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# 만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

# >>> import mod1
# >>> mod1.__name__
# 'mod1'


### 클래스나 변수 등을 포함한 모듈
# mod2.py 
# PI = 3.141592

# class Math: 
#     def solv(self, r): 
#         return PI * (r ** 2) 

# def add(a, b): 
#     return a+b

import mod2
print(mod2.PI) # 3.141592

a = mod2.Math()
print(a.solv(2)) # 12.566368

print(mod2.add(mod2.PI, 4.4)) # 7.541592


# **[모듈을 불러오는 또 다른 방법]**

# 우리는 지금껏 명령 프롬프트 창을 열고 모듈이 있는 디렉터리로 이동한 다음에 모듈을 사용할 수 있었다.
# 이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법에 대해 알아보자.

# 먼저 다음과 같이 이전에 만든 mod2.py 파일을 C:\doit\mymod로 이동시킨다.

# C:\Users\pahkey>cd C:\doit
# C:\doit>mkdir mymod
# C:\doit>move mod2.py mymod
#         1개 파일을 이동했습니다.
# 그리고 다음 예를 따라 해 보자.

# 1. sys.path.append(모듈을 저장한 디렉터리) 사용하기

# 먼저 sys 모듈을 불러온다.

# C:\doit>python
# >>> import sys
# sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. sys에 대해서는 뒤에서 자세하게 다룰 것이다.
# 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.

# 다음과 같이 입력해 보자.

# >>> sys.path
# ['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
# 'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.
# 만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다.
# 그렇다면 sys.path에 C:\doit\mymod 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있지 않을까?

# ※ 명령 프롬프트 창에서는 /, \든 상관없지만, 소스 코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.

# 당연하다. sys.path의 결괏값이 리스트이므로 우리는 다음과 같이 할 수 있다.

# >>> sys.path.append("C:/doit/mymod")
# >>> sys.path
# ['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
# 'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages', 
# 'C:/doit/mymod']
# >>>
# sys.path.append를 사용해서 C:/doit/mymod라는 디렉터리를 sys.path에 추가한 후 다시 sys.path를 보면 가장 마지막 요소에 C:/doit/mymod라고 추가된 것을 확인할 수 있다.

# 자, 실제로 모듈을 불러와서 사용할 수 있는지 확인해 보자.

# >>> import mod2
# >>> print(mod2.add(3,4))
# 7
# 이상 없이 불러와서 사용할 수 있다.

# 2. PYTHONPATH 환경 변수 사용하기

# 모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.

# 다음과 같이 따라 해 보자.

# C:\doit>set PYTHONPATH=C:\doit\mymod
# C:\doit>python
# >>> import mod2
# >>> print(mod2.add(3,4))
# 7
# set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를 설정한다.
# 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.