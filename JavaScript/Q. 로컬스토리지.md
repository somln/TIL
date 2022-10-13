# 로컬스토리지

### 1. 브라우저 저장 공간
* Local Storage:  key-value 형태로 문자, 숫자 데이터 저장가능, 브라우저를 재접속해도 남아있음
* Session Storage: key-value 형태로 문자, 숫자 데이터 저장가능, 브라우저를 재접속 하면 날라감
* Indexed DB:크고 많은 구조화된 데이터를 DB처럼 저장가능
* Cookies: 유저 로그인정보 저장공간
* Cache Storage: html css js img 파일 저장해두는 공간

<br>

### 2. 로컬스토리지 사용법
```js
localStorage.setItem('이름', 'kim') //자료저장하는법
localStorage.getItem('이름') //자료꺼내는법
localStorage.removeItem('이름') //자료삭제하는법
```
로컬스토리지에는 문자, 숫자만 저장이 가능하여 array, object 형태의 자료는 저장시 문자로 강제로 변환되어 형태가 깨지게 된다. 따라서 array, object 형태로 데이터를 저장하고 싶을 때는 JSON 형식으로 바꿔서 저장한 후 다시 꺼낼 때는 array, object 형식으로 바꿔주면 된다.
 ```js
var arr=[1,2,3]; 
var newArr=JSON.stringify(arr);  //arr을 JSON형식으로 저장
localStorage.setItem('num',newArr); //newArr를 로컬스토리지에 저장
var reArr=JSON.parse(newArr); //JSON을 arr형식으로 변환
console.log(reArr); //출력하면 원래 array 형식대로 출력됨
```