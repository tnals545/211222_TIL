# 리눅스_하둡\_스파크\_몽고DB

### 1. 가상화란?

- https://m.blog.naver.com/ilikebigmac/222009981745



### 2. Oracle VirtualBox 설치

- https://www.virtualbox.org/wiki/Downloads

![image-20211223141036624](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223141036624.png)

1\) Windows 전용

2\) Mac OS전용



### 3. 가상환경에 리눅스 설치

- http://mirror.anigil.com/CentOS/7.9.2009/isos/x86_64/

1. CentOS-7-x86_64-DVD-2009.iso 설치

![image-20211223141104020](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223141104020.png)

2. 다운받은 CentOS-7-x86_64-DVD-2009.iso 파일 바탕화면에 배치

3. VirtualBox 실행

4. 새로 만들기

5. 이름 : linux, 머신폴더 : 본인 파일 위치 확인, 종류 : linux, 버전 선택 : Red Hat(32bit or 64bit 선택)

![image-20211223141011291](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223141011291.png)



6. 메모리 크기 : 1024 >> 2048MB 변경

![image-20211223141000517](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223141000517.png)



7. 하드디스크 설정

![image-20211223140946337](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223140946337.png)



8. 하드디스크 파일 종류 설정

![image-20211223140905866](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223140905866.png)



9. 물리적 하드 드라이브에 저장

![image-20211223141819422](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223141819422.png)

- **동적 할당** : 하드디스크 파일은 가상 디스크를 사용할 때 **_고정된 최대 크기까지_** 파일 크기가 커지지만, 사용량이 줄어들어도 자동적으로 작아지지는 않음
- **고정 크기** : 하드디스크 파일은 만드는 데 더 오래 걸리지만 사용할 때 더 빠름



10. 파일 위치 및 크기 설정

![image-20211223142049651](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223142049651.png)

- 파일 크기 설정 후 만들기 클릭



11. 설치 완료

![image-20211223142132055](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20211223142132055.png)