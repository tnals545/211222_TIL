# 211224_기온 데이터 분석 코드

### 1. data준비

- 공공데이터 불러오기

```python
import csv

f = open('C:/Users/tnals/multicampus/code/data/seoul.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter = ',')
# print(data)
for row in data:
    print(row)
f.close()
```

```python
# output

['\t\t108', '서울', '2008-01', '-1.7', '1.9', '7.3', '2008-01-06', '-5.0', '-11.1', '2008-01-17']
['\t\t108', '서울', '2008-02', '-1.2', '3.2', '10.5', '2008-02-22', '-4.9', '-10.1', '2008-02-13']
['\t\t108', '서울', '2008-03', '7.3', '11.9', '19.8', '2008-03-21', '3.7', '-1.7', '2008-03-05']

...

['\t\t108', '서울', '2021-12', '', '', '13.3', '2021-12-08', '', '-11.2', '2021-12-18']
```



- data columns 추출

```python
import csv

f = open('C:/Users/tnals/multicampus/code/data/seoul.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter = ',')
header = next(data)
print(header)
f.close()
```

```python
# output

['\t\t지점번호', '지점명', '일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', '평균최저기온(℃)', '최저기온(℃)', '최저기온일자']
```



- data에서 최고기온 실수로 변환하기

```python
# 1. 데이터에서 최고 기온을 실수로 변환, 한 행씩 출력

import csv

f = open('C:/Users/tnals/multicampus/code/data/seoul.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter = ',')
header = next(data)
# print(header)
for row in data:
    row[5] = float(row[5]) # 최고 기온을 실수로 변환
    print(row)
f.close()
```

```python
#output

['\t\t108', '서울', '2008-01', '-1.7', '1.9', 7.3, '2008-01-06', '-5.0', '-11.1', '2008-01-17']
['\t\t108', '서울', '2008-02', '-1.2', '3.2', 10.5, '2008-02-22', '-4.9', '-10.1', '2008-02-13']
['\t\t108', '서울', '2008-03', '7.3', '11.9', 19.8, '2008-03-21', '3.7', '-1.7', '2008-03-05']

...

['\t\t108', '서울', '2021-12', '', '', 13.3, '2021-12-08', '', '-11.2', '2021-12-18']
```



### 2. 2008년부터 지금까지 중에 최고 기온과 그 날짜 찾기

```python
import csv

# 공공데이터 파일 열기
f = open('C:/Users/tnals/multicampus/code/data/seoul.csv', 'r', encoding='utf-8')
data = csv.reader(f)
header = next(data)
# print(header)

# 변수 만들기(초기화)
max_temp = -999
max_date = ''

for row in data:
    if row[5] == '': # 누락된 결측치 처리
        row[5] = -999
    row[5] = float(row[5]) # str은 값을 서로 비교할 수 없기 때문에 최고 기온을 실수로 변환
    if max_temp < row[5]: # max_temp 값과 row[5](6번째 columns)에 있는 최고 기온 값을 비교하여 row[5]값이 더 크면
        max_date = row[6] # row[6](7번째 columns)에 있는 최고기온일자를 max_date 변수에 update하고
        max_temp = row[5] # row[5]에 있는 최고 기온을 max_temp 변수에 update함.
f.close()

print(max_temp, max_date)
print('2008년도 이후 서울 최고 기온이 가장 높았던 날은', max_date,'로,',max_temp,'도 였습니다.')
```

```python
#output
# 39.6 2018-08-01
# 2008년도 이후 서울 최고 기온이 가장 높았던 날은 2018-08-01 로, 39.6 도 였습니다.
```

