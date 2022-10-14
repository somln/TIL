# form 만들기(조건문)
>form이란 사용자가 웹페이지에 어떤 값을 입력했을 때 그 값을 서버로 넘겨주는 일을 하는 태그 혹은 위젯을 의미한다.

<br>

### 1. form 형태 만들기
```html
//action: 폼 내부에 데이터를 보내는 목적지 url을 지정
<form action="success.html">
//text 유형의 input 사용
    <div class="my-3">
      <input type="text" class="form-control" id="email">
    </div>
    <div class="my-3">
      <input type="password" class="form-control" id="pw">
//눌렀을 때 event 발생하는 button 생성
    </div>
    <button type="submit" class="btn btn-primary" id="send">전송</button>
    <button type="button" class="btn btn-danger" id="close">닫기</button>
</form> 
```
<br>

### 2. 전송 버튼 클릭 시 동작 JS로 작성(조건문 사용)
전송 버튼 클릭 시 동작:
1. 전송버튼 누를 때 아이디가 공백이면 '아이디를 입력하세요', 비밀번호가 공백이면 '비밀번호를 입력하세오' 출력하기         

2. 전송버튼 누를 때 입력한 비번이 6자 미만이면 알림띄우기

```js
$('#send').on('click', function(){
  if ($('#email').val() == '') {
      alert(' 아이디를 입력하세요');
  }
  if($('#pw').val() == '')
      alert('비밀번호를 입력하세요');
  }
  else if($('#pw').val().length <6){
       alert('비밀번호 6글자 이상 입력하세요');
  } 
ㄴ);     
 ```
 <br>

 ### 3. 전체 코드

  ```html
  //index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    <div class="black-bg">
        <div class="white-bg">
          <h4>로그인하세요</h4>
          <form action="success.html">
            <div class="my-3">
              <input type="text" class="form-control" id="email">
             </div>
             <div class="my-3">
                <input type="password" class="form-control" id="pw">
             </div>
             <button type="submit" class="btn btn-primary" id="send">전송</button>
             <button type="button" class="btn btn-danger" id="close">닫기</button>
          </form> 
        </div>
      </div> 

      <div class="main-bg">
        <h4>Shirts on Slae</h4>
        <button id="login" class="btn btn-danger">로그인</button>
    </div>

    <script
    src="https://code.jquery.com/jquery-3.6.1.min.js"
    integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ="
    crossorigin="anonymous"></script>

    <script>
        $('#login').on('click', function(){
            $('.black-bg').addClass('show-modal');
         });
    
         $('#close').on('click', function(){
            $('.black-bg').css('display', 'none');
         });

         $('#send').on('click', function(){
            if ($('#email').val() == '') {
                alert(' 아이디를 입력하세요');
            }
            if($('#pw').val() == '') {
                alert('비밀번호를 입력하세요');
            }
            else if($('#pw').val().length <6){
                alert('비밀번호 6글자 이상 입력하세요')
            }
        });         
        
    </script>
</body>
</html>
  ```
<br>

 ```css
 //style.css
.black-bg {
    width : 100%;
    height : 100%;
    position : fixed;
    background : rgba(0,0,0,0.5);
    z-index : 5;
    padding: 30px;
    display:none;
  }
  .white-bg {
    background: white;
    border-radius: 5px;
    padding: 30px;
  } 

  .show-modal {
    display:block;
    opacity: 1;
  }

  .main-bg{
    padding:100px 20px;
    background: lightgrey;
  }
  
  .btn{
    background-color:red;
    color:white;
    border: none;
  }
   ```

