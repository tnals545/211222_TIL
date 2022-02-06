# class

import pandas as pd
import numpy as np

## 계산기 만들기
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

## 계산기 2개 만들기
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

## 계산기가 점점 더 많이 필요해질 때 class 사용
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

    ## 빼기 기능 추가시
    def sub(self, num):
        self.result -= num
        return self.result

    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

## 사칙연산 class 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

a.add()
a.mul()
a.sub()
a.div()

b.add()
b.mul()
b.sub()
b.div()

## 생성자(Constructor) -> __init__
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first)
print(a.second)
a.add()
a.div()

## class의 상속(Inheritance)
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
a.add()
a.mul()
a.sub()
a.div()

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.pow()

## 메서드 오버라이딩(Overriding, 덮어쓰기)
a = FourCal(4, 0)
a.div()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 18, in div
# ZeroDivisionError: division by zero

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            self.first / self.second

a = SafeFourCal(4, 0)
a.div()

## class 변수
class Family:
    lastname = '김'

print(Family.lastname)
# class 변수는 위와 같이 class이름.class변수 로 사용 가능
# 또는 Family 클래스를 아래와 같이 사용 가능
a = Family()
b = Family()
print(a.lastname) # 김
print(b.lastname) # 김

Family.lastname = '박'
print(a.lastname) # 박
print(b.lastname) # 박
# 클래스 변수는 클래스로 만들어진 모든 객체에 공유됨

# id함수를 사용하여 클래스 변수가 공유된다는 사실 증명 가능
id(Family.lastname) # 2363460139120
id(a.lastname) # 2363460139120
id(b.lastname) # 2363460139120