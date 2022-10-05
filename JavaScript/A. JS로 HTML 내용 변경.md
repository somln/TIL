# JS로 HTML 내용 변경
>자바스크립트는 HTML 조작을 위해 사용한다.

HTML 조작, 변경을 위해서는 3가지를 정해주어야 한다.   
* 변경할 요소    
* 변경할 요소의 속성    
* 변경 내용     
 <br>

 예를 들어,
```js
document.getElementById('title').innerHTML='JS';
```
의 코드를 해석하자면,    
>document -> html 웹문서    
>. -> ~의     
>getElementById('title') -> 아이디가 'title'인 html 요소를 찾아라       
>innerHTML -> 내부 HTML을      
>'JS' -> 'JS'으로 바꿔라

<br>

같은 원리로
``` js
document.getElementByTagName('h1).style.fontSize='16px';
``` 
문서의 태그가 h1인 요소의 폰트 사이즈를 16으로 바꿔라.    
```js
document.getElementsByClassName('alert').style.display=block;
```
문서의 클래스가  alert인 요소의 display를 block으로 바꿔라.

<br>

### DOM에서 원하는 요소를 찾는 방법
* getElementById(): 괄호 안에 아이디명 입력
* getElementsByClassName(): 괄호 안에 클래스명 입력; 인덱스를 사용하여 원하는 부분 선택
* querrySeloctor(): 괄호안에 css문법대로 요소 작성; 맨 처음에 오는 요소만 선택됨
* querySelectorAll(): 괄호안에 css문법대로 요소 작성; 인덱스를 사용하여 원하는 부분 선택