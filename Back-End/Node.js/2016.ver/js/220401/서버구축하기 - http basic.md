# 서버구축하기 - http basic

- 이번장부터는 node.js 의 http 모듈을 사용하여 간단한 웹서버를 구축해보고 브라우저를 통해 접속해 보겠습니다.





### 가. 서버구축 용 프로젝트 폴더 생성

1. 먼저 서버 구축을 하기위해 프로젝트 폴더를 생성
   - 새 폴더 또는 mkdir 로 폴더를 생성
     - 윈도우계열이라면 C드라이브 또는 D드라이브의 최상위(Root) 경로에 workspaces 폴더를 생성하고 그 아래에 nodejs 폴더를 생성
     - 대다수의 개발자들이 한 가지 언어나 툴만 사용하지 않기 때문에 해당 언어나 툴별로 workspaces 를 정리해두면 이 후에 프로젝트가 많아져도 관리가 편해짐

![img](https://javafa.gitbooks.io/nodejs_server_basic/content/assets/chapter3_folder_structure.png)



2.  nodejs 폴더 아래에 실제 사용할 프로젝트를 생성

![img](https://javafa.gitbooks.io/nodejs_server_basic/content/assets/chapter3_create_folder.png)





### 나. server.js 파일 생성

- server_basic 폴더 아래에 server.js 파일을 생성하고 아래와 같이 내용을 입력



*server.js*

```js
// 1. 서버 사용을 위해서 http 모듈을 http 변수에 담는다. (모듈과 변수의 이름은 달라도 된다.) 
var http = require('http'); 

// 2. http 모듈로 서버를 생성한다.
//    아래와 같이 작성하면 서버를 생성한 후, 사용자로 부터 http 요청이 들어오면 function 블럭내부의 코드를 실행해서 응답한다.
var server = http.createServer(function(request,response){ 

    response.writeHead(200,{'Content-Type':'text/html'});
    response.end('Hello node.js!!');

});

// 3. listen 함수로 8080 포트를 가진 서버를 실행한다. 서버가 실행된 것을 콘솔창에서 확인하기 위해 'Server is running...' 로그를 출력한다
server.listen(8080, function(){ 
    console.log('Server is running...');
});
```





### 다. server.js 실행 및 접속

- CMD(mac은 터미널) 또는 명령어 실행창을 실행
  - 위의 코드를 작성한 server_basic 폴더로 이동한 후에 위에 작성한 코드를 실행

![img](https://javafa.gitbooks.io/nodejs_server_basic/content/assets/chapter3_cmd1.png)



- 웹 브라우저에서 주소창에 다음과 같이 입력한 후 접속

[http://localhost:8080](http://localhost:8080/)

![image-20220402190347119](C:\Users\tnals\AppData\Roaming\Typora\typora-user-images\image-20220402190347119.png)





### 라. 소스코드 분석

- 웹서버를 실행하기 위해서 http 모듈을 require로 불러옴
  - require는 다른언어의 import 와 유사한 기능

- node.js 는 require 후에 해당 모듈을 http 라는 변수에 담은 후 하나의 독립적인 객체로 사용

```js
var http = require('http');
```



- http 모듈에 정의되어 있는 createServer 함수로 서버를 생성

```js
function nameOfFunction(parameters) {
    // 실행로직
}
```



- createServer( ) 에 파라미터로 입력되는 function(request,response){ } 은 함수명이 없음

- 함수명이 없이 function 이라고만 작성된 파라미터는 이벤트 발생시에 callback
- 즉, 생성된 서버로 어떤 요청이 들어오면 function 내부의 로직이 실행되면서 function 내부에 선언한 request와 response라는 이름으로 사용할 수 있는 값을 넘겨줌
- 그래서 function 블럭 { } 내부에서는 request 와 response로 넘어오는 어떤 값을 사용할 수 있게 됨

```js
var server = http.createServer( function(request,response) { 

    response.writeHead(200,{'Content-Type':'text/html'});
    response.end('Hello node.js!!');

});
```



- function 내부 로직을 살펴보면 response로 넘어온 값으로 함수를 실행
  - 즉 callback 되었을 때 response 에 담겨저 오는 값은 require로 가져온 http 모듈처럼 내부적으로 함수를 가지고 있는 객체라는 의미

- 여기서 **response 객체**는 서버로 웹브라우저나 또는 앱으로 부터 어떤 요청이 있을 때 요청한 사용자 측으로 값을 반환해 줄 때 사용하는 객체
- 반대로 **request 객체**는 사용자가 요청한 내용이 담겨있는 객체

- 아래 코드에서는 response 객체를 사용해 사용자 측으로 반환값을 넘겨주는데, 먼저 writeHead( ) 라는 함수에 첫번째는 200 이라는 숫자값을, 두번째는 { } 중괄호 안에 { '키' : '값' } 형태의 값을 담음

```js
response.writeHead(200, {'Content-Type':'text/html'});
```



1. 200
   - 첫번째 200 이라는 숫자값은 웹서버 들어오는 어떤 요청에 대해 정상적으로 값을 리턴할 때 사용하는 http 상태코드
   - 오류가 없이 서버에서 처리가 정상적으로 완료되면 200 코드를 담아서 응답헤더를 설정
   - 여기서 응답헤더를 브라우저를 예로 들어 설명하면 서버로 부터 반환되는 값의 대한 기본 정보를 담고 있는 것으로 브라우저 화면에는 나타나지 않는 값
   - 브라우저는 header 값을 보고 서버에서 넘어온 값이 어떤 형태인지를 파악하고 실제 값을 header 에 세팅된 설정에 맞게 보여줌



2. {'Content-Type' : 'text/html'}

   - 두번째 {'Content-Type' : 'text/html'} 값은 서버측에서 보내주는 컨텐츠의 타입이 텍스트이고, html 형태라는 것을 정의
   - 브라우저에서는 이 헤더를 기준으로 아래 코드에서 보여주는 값을 html 형태로 화면에 출력
   - 이렇게 { } 블럭형태로 값이 전달되는 경우는 해당 블럭에 복수개의 값이 담길 수 있다는 의미
   - 차후에 예제로 진행하겠지만 두번째 값은 Content-Type 이라는 키값 이외에도 Authorization, Cookie 등의 다양한 값들을 지정할 수 있음

   - 아래코드는 end( ) 라는 함수에 'Hello node.js!!'라는 실제 컨텐츠를 담아서 브라우저 측에 전달

   - 이렇게 실제 코드 값을 end( ) 함수로 전달하면 브라우저는 해당 컨텐츠를 받은 후 html 형태로 화면에 출력

```js
response.end('Hello node.js!!');
```