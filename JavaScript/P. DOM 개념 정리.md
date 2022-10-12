# DOM 개념정리 
 

### 1. DOM이란?
>자바스크립트가 HTML에 대한 정보들 (id, class, name, style, innerHTML 등)을 object 자료로 정리한 것 

자바스크립트는 html에 특화된 언어이지만, html 문법을 직접 해석하고 조작할 수 없다. 따라서 자바스크립트가 HTML 조작을 하기 위해선 HTML을 자바스크립트가 해석할 수 있는 문법으로 변환해놓아야 한다.

브라우저는 HTML 페이지를 열어줄 때, HTML을 자바스크립트로 쉽게 찾고 바꾸기 위해 object와 비슷한 자료형에 담아둔다. 예를 들어서 
```html
<div style="color : red">안녕하세요</div>
``` 
▼ 아래 변수를 Document Object Model이라고 한다
```js
var document = {
  div1 : {
    style : {color : 'red'}
    innerHTML : '안녕하세요'
  }
}
```
실제 생김새는 다르지만, 이런 식으로 object 자료에 정리를 해놓으면,
document.div1.innerHTML = '안녕' 이렇게 자바스크립트를 짜면 HTML 조작이 가능하다.

<br>

### 2. DOM 생성순서

>브라우저는 HTML문서를 위에서 부터 차례로 읽어내려간다. 읽을 때 마다 HTML을 발견하면 DOM에 추가해준다.

따라서, 아래와 같이 코드를 짜면 애러가 발생한다.

```html
<script>
  document.getElementById('test').innerHTML = '안녕'
</script>

<p id="test">임시글자</p>
```

id가 test인 p태그에 대한 DOM이 아직 생성되지 않은 상태에서 자바스크립트로 해당 부분을 바꾸려고 하기 때문에 애러가 발생한다.

<br>

### 3. 자바 스크립트 실행을 나중으로 미루기
>"이 코드는 HTML 전부 다 읽고 실행해주세요" 라고 코드짜놓으면 위와 같은 애러가 발생하지 않는다.
```js
$(document).ready(function(){ 실행할 코드 })
document.addEventListener('DOMContentLoaded', function() { 실행할 코드 }) \
```
이 이벤트리스너들은 "HTML을 다 읽어들였는지"를 알려주는 이벤트리스너이다.

```html
<script>
  document.addEventListener('DOMContentLoaded', function() { 
    document.getElementById('test').innerHTML = '안녕'
  })
</script>

<p id="test">임시글자</p>
```
따라서 위와 같이작성하면, id가 test인 p태그의 html은 '안녕'으로 변경된다.

<br>

### 4. load 이벤트리스너
>load 라는 이벤트리스너를 사용하면 DOM 생성뿐만 아니라 이미지, css, js파일이 로드가 됐는지도 체크가능하다.

```js
$(window).on('load', function(){
  //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드 
});

window.addEventListener('load', function(){
  //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드
})
```
