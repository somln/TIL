# 스크롤 이벤트

> 스크롤 이벤트를 이용하면, 스크롤바를 조작할 때 마다 코드실행이 가능하고, 박스의 숨겨진 실제 높이와 스크롤을 내린 양 등을 구할 수 있다.

<br>

### 1. 스크롤 이벤트 함수

페이지 전체에서
* window.scrollY:현재 페이지를 얼마나 위에서 부터 스크롤했는지 px 단위로 반환
* window.scrollTo(0, 100): 위에서부터 100px 위치로 스크롤
* window.scrollBy(0, 100): 현재 위치에서부터 +100px 만큼 스크롤

원하는 태그(class, id)에서
* document.querySelector('.box').scrollTop: 스크롤바를 위에서 부터 얼마나 내렸는지
* document.querySelector('.box').scrollHeight: 스크롤 시키지 않았을때 창 전체 높이
* document.querySelector('.box').clientHeight: 눈에 보이는 많큼의 창 높이

<br>

### 2.  페이지의 스크롤바를 100px 내리면 로고 폰트사이즈 작게 만들기

```js
$(window).on('scroll', function(){ //스크롤 이벤트 발생시 실행

    var scrollVal=$(window).scrollTop(); 

    if(scrollVal>100){  //스크롤 바를 100px 이상 내렸을 경우
        $('.navbar-brand').css('font-size', '15px');  //폰트 사이즈 변경
    }
    else
    $('.navbar-brand').css('font-size', '30px');

});
```
<br>

### 3. 박스 끝까지 스크롤시 알림띄우기

```js
$('.lorem').on('scroll', function(){  //'.lorem'태그의 창을 스크롤 했을 시 실행

    var scrollVal2=document.querySelector('.lorem').scrollTop; //스크롤 바 내린 양 저장
    var scrollH=document.querySelector('.lorem').scrollHeight; //전체 창의 높이 저장
    var height=document.querySelector('.lorem').clientHeight; //보이는 창의 높이 저장

//전체 창의 높이=스크롤 바 내린양+ 보이는 창의 높이 일  경우 창을 끝가지 내린 것
//오류 발생을 막기 위해 = 대신 >사용
    if(scrollVal2+height>scrollH-10){ 
        alert("확인");
    }
});
```

<br>

### 4. 전체 코드

```html
//index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>  
    
    <nav class="navbar navbar-light bg-light">
    <div class="container-fluid">
      <span class="navbar-brand">Navbar</span>
      <button class="navbar-toggler" type="button">
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
  </nav> 

  <div style="height: 100px"></div>

  <div class="lorem" style=" width: 200px; height: 100px; overflow-y: scroll">
    Lorem ipsum dolor sit amet, consectetur 
    adipisicing elit. Quae voluptas voluptatum minus praesentium
    fugit debitis at, laborum ipsa itaque placeat sit, excepturi eius.
    Nostrum perspiciatis, eligendi quae consectetur praesentium exercitationem.</div>

  <div style="height: 900px"></div>

<script
src="https://code.jquery.com/jquery-3.6.1.min.js"
integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ="
crossorigin="anonymous"></script>

<script>

$(window).on('scroll', function(){

    var scrollVal=$(window).scrollTop();

    if(scrollVal>100){
        $('.navbar-brand').css('font-size', '15px');
    }
    else
    $('.navbar-brand').css('font-size', '30px');

});


$('.lorem').on('scroll', function(){
    var scrollVal2=document.querySelector('.lorem').scrollTop;
    var scrollH=document.querySelector('.lorem').scrollHeight;
    var height=document.querySelector('.lorem').clientHeight;
    if(scrollVal2+height>scrollH-10){
        alert("확인");
    }
});

</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
```

```css
/* style.html */
.navbar {
  position : fixed;
  width : 100%;
  z-index : 5
}

.navbar-brand {
  font-size : 30px;
  transition: all 1s;
}
```
