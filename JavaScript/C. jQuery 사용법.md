# jQuery 사용 방법
>jQuery를 사용하면 복잡한 JavaScript 코드를 보다 간단하게 만들 수 있다.

<br>

### 1. jQuery 선언           
해당 코드를 html 파일에 붙여넣는다.
```js
<script
  src="https://code.jquery.com/jquery-3.6.1.min.js"
  integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ="
  crossorigin="anonymous"></script>
```
<br>

### 2. jQuery 문법
```
$(선택자).동작함수();
```

<br>

### 3. 사용 예시

* html 내용변경
```js
<p class="p1">JS</p>

<script>
  $('.p1').html('jQuery'); 
</script>
```

* 스타일 변경
```js
<p class="p1">JS</p>

<script>
 $('.p1').css('color', 'red'); 
</script>
```

*  class 탈부착
```js
<script>
  $('.p1').addClass('클래스명');
  $('.p1').removeClass('클래스명');
  $('.p1').toggleClass('클래스명');
```

* html 여러개 변경
```js
<script>
<p class="p1">안녕</p>
<p class="p1">안녕</p>
<p class="p1">안녕</p>

<script>
  $('.p1').html('안녕하세요');
</script>
```

* 이벤트 리스너
```js
<p class="p1">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
  });
</script>
```

* UI 애니매이션

```js
<p class="p1">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
    $('.p1').fadeOut();
  });
</script>
```

<br>

----------------------

<br>

* jQuery를 적용하여 모달창 만들기
```html
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
          <button class="btn btn-danger" id="close">닫기</button>
        </div>
      </div> 
      <button id="login">로그인</button>

      <script
    src="https://code.jquery.com/jquery-3.6.1.min.js"
    integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ="
    crossorigin="anonymous"></script>

    <script>
    $('#login').on('click', function(){
        $('.black-bg').addClass('show-modal');
     });

     $('#close').on('click', function(){
        $('.black-bg').css('display', 'none')
     });
    </script>
 
</body>
</html>
```

```css
.black-bg {
    width : 100%;
    height : 100%;
    position : fixed;
    background : rgba(0,0,0,0.5);
    z-index : 5;
    padding: 30px;
    display: none;
  }
  .white-bg {
    background: white;
    border-radius: 5px;
    padding: 30px;
  } 

  .show-modal {
    display : block;
  }
  
  ```