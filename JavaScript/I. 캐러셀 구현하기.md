# 캐러셀 구현하기
>캐러셀은 이미지나 텍스트의 슬라이드를 가로로 슬라이드시켜 여러 개를 표시하는 컴포넌트이다.

<br>

### 1. 시작스타일 만들기 (class로)
```html
//index.html
<div style="overflow: hidden">
        <div class="slide-container">
          <div class="slide-box">
            <img src="car1.png">
          </div>
          <div class="slide-box">
            <img src="car2.png">
          </div>
          <div class="slide-box">
            <img src="car3.png">
          </div>
        </div>
    </div>

    <button class="slide-1">1</button>
    <button class="slide-2">2</button>
    <button class="slide-3">3</button>
    <button class="slide-next">다음</button>
    <button class="slide-prev">이전</button>

```

```css
/* style.css */
.slide-container {
  width: 300vw;
}
.slide-box {
  width: 100vw;
  float: left;
}
.slide-box img {
  width: 100%;
} 
```

<br>

### 2. 최종스타일 만들기 (class로) 
```css
.slide-container {
  width: 300vw;
  transform: translateX(-100%);
}
  
```

<br>

### 3. 원할 때 최종스타일로 변하라고 JS 코드짜기
```js
 var page=1;

        //1번 버튼 클릭
        $('.slide-1').on('click', function() {
        $('.slide-container').css('transform', 'translateX(0vw)');
        page=1;
       });

       //2번 버튼 클릭
       $('.slide-2').on('click', function() {
        $('.slide-container').css('transform', 'translateX(-100vw)');
        page=2;
       });

       //3번 버튼 클릭
       $('.slide-3').on('click', function() {
        $('.slide-container').css('transform', 'translateX(-200vw)');
        page=3;
       });

       //다음 버튼 클릭
       $('.slide-next').on('click', function() {
        if(page==1){
            $('.slide-container').css('transform', 'translateX(-100vw)');
            page=2;
        }
        else if(page==2){
            $('.slide-container').css('transform', 'translateX(-200vw)');
            page=3;
        }
       });

       //이전 버튼 클릭
       $('.slide-prev').on('click', function() {
        if(page==3){
            $('.slide-container').css('transform', 'translateX(-100vw)');
            page=2;
        }
        else if(page==2){
            $('.slide-container').css('transform', 'translateX(0vw)');
            page=1;
        }
       });
```

<br>

### 4. 시작스타일에 transition 추가 
```css
.black-bg {
    ..생략..
    transition: all 1s;
  }
```

<br>

+ 확장성 좋은 다음, 이전버튼으로 업데이트

```js
$('.slide-next').on('click', function() {
    $('.slide-container').css('transform', 'translateX(-'+page+'00vw)')
        page++;
    });

$('.slide-prev').on('click', function() {
    $('.slide-container').css('transform', 'translateX(-'+(page-2)+'00vw)')
        page--;
    });
```

<br>

--------------------------------------------------------------------------

<br>

## 스와이프 기능
> 스와이프: 터치 혹은 클릭을 한 후, 일직선으로 드래그하는 것

### 1. mouse 이벤트
* mousedown: 어떤 요소에 마우스버튼 눌렀을 때
* mouseup: 어떤 요소에 마우스버튼 뗐을 때
* mousemove: 어떤 요소위에서 마우스 이동할 때
```
//마우스가 이동할 때 마다 콘솔에 마우스 x의 좌표 출력하기
$('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX)
  })
```

<br>

### 2. 스와이프 기능 구현하기
 1. 사진1을 왼쪽으로 드래그한 거리만큼 사진1도 왼쪽으로 움직이도록 작성
 2. 마우스를 땠을 때 이동 거리가 300이상이면 사진2, 300 미만이면 사진 1 보여주도록 작성

 ```js
  var startX = 0; //마우스 클릭 위치
  var check=false;  //마우스를 누른 상태인지 표시

$('.slide-box').eq(0).on('mousedown', function(e){  //마우스를 클릭했을 때
  startX = e.clientX; //클릭 위치 저장
  check=true;  //마우스 누른 상태
});

$('.slide-box').eq(0).on('mousemove', function(e){  //마우스를 움직일 때
  console.log(e.clientX - startX)
  if(check==true){  //마우스를 누른 상태이면
    $('.slide-container').css('transform', `translateX( ${e.clientX - startX}px )`)  //이동거리만큼 그림 이동
  }
  
});

$('.slide-box').eq(0).on('mouseup', function(e){  //마우스를 땠을 때
    check = false;  //마우스를 누르지 않은 상태

    if (e.clientX -startX <= -300) {  //오른쪽으로 이동한 거리가 300 이상이면
      $('.slide-container').css('transition', 'all 1s').css('transform', 'translateX(-100vw)'); //다음 그림으로 이동
    } else {  //오른쪽으로 이동한 거리가 300 미만이면
      $('.slide-container').css('transition', 'all 1s').css('transform', 'translateX(0vw)');  //다시 첫번째 그림으로 이동
    }

    //평소엔 transition이 필요가 없는데 사진에서 사진에서 마우스를 떼면 transition이 필요함 
    //"마우스 떼면 잠깐 1초정도 transition 붙였다가 제거하라는 코드를 작성해야 함
    setTimeout(function(){  
      $('.slide-container').css('transition', 'none')
     }, 1000);
  });
  
```
