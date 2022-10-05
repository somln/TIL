# 동적 UI 만들기(함수, 이벤트)

> 기본적인 UI 만드는 규칙
>1. HTML CSS 로 미리 UI 디자인을 해놓고 필요하면 평소엔 숨긴다.
>2. 버튼을 누르거나할 경우 UI를 보여달라고 자바스크립트 코드를 짠다.

<br><br>

D 1. html, css로 알림창 디자인  

html 파일    
```html
<div class="alert-box" id="alert">알림창</div>
```
css 파일     
```css
.alert-box {
  background-color: skyblue;
  padding: 20px;
  color: white;
  border-radius: 5px;
  display: none; //평소에는 숨겨놓기
} 
```
<br>

### 2. javascipt로 버튼 누르면 알림창이 뜨도록 설정

```js
<button onclick="document.getElementById('alert').style.display=block;>버튼</button>
 ``` 
or
 ``` js
 .show{
    display:block;
 }
 
<button onclick="document.getElementById('alert').classList.add('show');>버튼</button>
 ``` 
--여기까지 기본적인 동적 UI 완성<br>

---------------------
<br><br>

* 닫기 버튼 추가하기
```html
   <div class="alert-box" id="alert">
    알림창  
    <button onclick="document.getElementById('alert').style.display=block;">닫기</button>     
    </div>
 ``` 
<br><br>

* 함수 적용하기
 ``` html
<div class="alert-box" id="alert">
    알림창
    <button onclick="alertDisplay('none');">닫기</button>
    </div>

    <button onclick="alertDisplay('block'); ">버튼</button>

 <script>
        function alertDisplay(bn){
            document.getElementById('alert').style.display=bn;
        }
</script>
 ``` 

 <br><br>

* 버튼 1을 눌렀을 때 "아이디를 입력하세요" 출력   
  버튼 2를 눌렀을 때 "비밀번호를 입력하세요" 출력

 ```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="alert-box" id="alert">
    <p id="title">알림창</p>
    <button onclick="alertDisplay('none');">닫기</button>
    </div>

    <button onclick="alertDisplay('block'); alertMessage('아이디를 입력하세요')">버튼1</button>
    <button onclick="alertDisplay('block'); alertMessage('비번을 입력하세요')">버튼2</button>

    <script>
        function alertDisplay(bn){
            document.getElementById('alert').style.display=bn;
        }

        function alertMessage(message){
            document.getElementById('title').innerHTML=message;
        }
    </script>
    </body>
</html>
 ``` 
 <br>

---------------------

 <br><br>

 >이벤트 리스너:    
 >html 안에 javascript 코드를 넣는 방식이 아닌, addEventListener()를 사용하여 이벤트를 등록할 수 있다.

 <br>

* 사용 방법 

``` js
document.getElementById('btn').addEventListener('click', function(){     
   });
   //document.getElementById(아이디 이름).addEventListener(이벤트이름, 함수이름 or 함수 작성)
 ```

<br>

* 이벤트 리스너 적용하기

 ``` html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Document</title>
   <link rel="stylesheet" href="main.css">
</head>
<body>
   <div class="alert-box" id="alert">
   <p id="title">알림창</p>
   <button id="close";>닫기</button>
   </div>

   <button id="inputID">버튼1</button>
   <button id="inputPW">버튼2</button>

   <script>
    document.getElementById('close').addEventListener("click", function(){ alertDisplay('none');});
    document.getElementById('inputID').addEventListener("click", function(){ alertDisplay('block'), alertMessage("아이디를 입력하세요");});
    document.getElementById('inputPW').addEventListener("click", function(){ alertDisplay('block'), alertMessage("비밀번호를 입력하세요");});

       function alertDisplay(bn){
           document.getElementById('alert').style.display=bn;
       }

       function alertMessage(message){
           document.getElementById('title').innerHTML=message;
       }
   </script>
   </body>
</html>
 ``` 
<br><br>



