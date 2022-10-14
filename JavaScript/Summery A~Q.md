# Summery A~Q

## 1.JS로 HTML 내용 변경
 ```js
 document.getElementById('title').innerHTML='JS';
 //html 웹문서의 아이디가 'title'인 html 요소를 찾아서 내부 HTML을 'JS'으로 바꿔라
 ```
 #### DOM에서 원하는 요소를 찾는 방법
* getElementById(): 괄호 안에 아이디명 입력
* getElementsByClassName(): 괄호 안에 클래스명 입력; 인덱스를 사용하여 원하는 부분 선택
* querrySeloctor(): 괄호안에 css문법대로 요소 작성; 맨 처음에 오는 요소만 선택됨
* querySelectorAll(): 괄호안에 css문법대로 요소 작성; 인덱스를 사용하여 원하는 부분 선택

 <br>

## 2. 동적 UI 만들기
#### 기본적인 UI 만드는 규칙
1. HTML CSS 로 미리 UI 디자인을 해놓고 필요하면 평소엔 숨긴다.

2. 버튼을 누르거나할 경우 UI를 보여달라고 자바스크립트 코드를 짠다.
 ```css
 .show{
   display:block;
}

<button onclick="document.getElementById('alert').classList.add('show');>버튼</button>
 ```
 <br>

## 3. jQuery 사용 방법

1. jQuery 선언
```html
<script
  src="https://code.jquery.com/jquery-3.6.1.min.js"
  integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ="
  crossorigin="anonymous"></script>
 ```

2. jQuery 문법
```js
$(선택자).동작함수();

$('.p1').html('jQuery'); 
$('.p1').css('color', 'red'); 
$('.p1').addClass('클래스명');
$('.p1').removeClass('클래스명');
$('.p1').toggleClass('클래스명');
$('.test-btn').on('click', function(){ });
```

 <br>

## 4. 간단한 애니매이션 만들기

1. 시작스타일 만들기 (class로)
2. 최종스타일 만들기 (class로)
3. 원할 때 최종스타일로 변하라고 JS 코드짜기
 ```js
     $('#login').on('click', function(){
        $('.black-bg').addClass('show-modal');
     });
 ```
4. 시작스타일에 transition 추가
 ```css
 .black-bg {
    ..생략..
    transition: all 1s;
  }
 ```
 ### ※ css 디자인할 때 유용한 라이브러리     
[Bootstrap](https://getbootstrap.com/)               
사용 방법:       
* css 파일은 해드 태그 안에 입력
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

 * js 파일은 바디 태그 끝나기 전에 입력
 ```html
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
  ```

 <br>

## 5.form 만들기
1. form 형태 만들기
2. 전송 버튼 클릭 시 동작 JS로 작성
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
); 
 ```

 <br>
 
## 6. 다크모드 설정하기
1. 다크모드 버튼 생성하기
2. 다크모드 클래스 만들기
3. 변수를 사용하여 토글
 ```js
    var count=0;
    $('.badge').on('click', function(){
      count++;
//버튼을 홀수번 눌렀을 경우
      if (count % 2 == 1) {
    $('.badge').html('Light 🔄');
    //버튼 글자 Light로 변경
    $('body').addClass('dark');
    //바디 태그에 dark 클래스 추가

//버튼을 짝수번 눌렀을 경우
  } else {
    $('.badge').html('Dark 🔄');
    //버튼 글자 Dark로 변경
    $('body').removeClass('dark');
    //바디 태그에 dark 클래스 제거
  }
});
 ``` 

 <br>

## 7. 타이머 기능
1. setTimeout & clearTimeout
:일정 시간 후에 특정 코드, 함수를 의도적으로 지연한 뒤 실행하고 싶을 때 사용하는 함수이다
 ```js
 let timer = setTimeout(function(){ }, delay);
 clearTimeout(timer)
 ```
2. setInterval & clearInterval
:일정 시간을 간격으로 콜백함수를 반복 호출 하는 함수이다.
 ```js
let interval = setInterval(function(){ }, delay);
clearInterval(interval);
 ```

 <br>

## 8.정규식
정규 표현식, 또는 정규식은 문자열에서 특정 문자 조합을 찾기 위한 패턴이다. js에서는 test()등의 메서드를 사용하는데, test() 메서드는 주어진 문자열이 정규 표현식을 만족하는지 판별하고, 그 여부를 true 또는 false로 반환한
 
 ```js
 /abc/.test('abcde');
//'abcde'안에 'abc'라는 문자가 있는지 여부에 따라 true, false 반환
```
문법 참고:
[regex](https://sooftware.io/regex/)

 <br>

## 9.캐러셀 구현하기
캐러셀은 이미지나 텍스트의 슬라이드를 가로로 슬라이드시켜 여러 개를 표시하는 컴포넌트이다.
1. 시작스타일 만들기 (class로)
2. 최종스타일 만들기 (class로)
3. 원할 때 최종스타일로 변하라고 JS 코드짜기
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

 ```
 4. 시작스타일에 transition 추가

### 마우스 이벤트   
mousedown: 어떤 요소에 마우스버튼 눌렀을 때              
mouseup: 어떤 요소에 마우스버튼 뗐을 때             
mousemove: 어떤 요소위에서 마우스 이동할 때              

 ```js
//마우스가 이동할 때 마다 콘솔에 마우스 x의 좌표 출력하기
$('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX)
  })
```

 <br> 

## 10. 스크롤 이벤트
스크롤 이벤트를 이용하면, 스크롤바를 조작할 때 마다 코드실행이 가능하고, 박스의 숨겨진 실제 높이와 스크롤을 내린 양 등을 구할 수 있다.
### 1. 스크롤 이벤트 함수

페이지 전체에서
* window.scrollY:현재 페이지를 얼마나 위에서 부터 스크롤했는지 px 단위로 반환
* window.scrollTo(0, 100): 위에서부터 100px 위치로 스크롤
* window.scrollBy(0, 100): 현재 위치에서부터 +100px 만큼 스크롤

원하는 태그(class, id)에서
* document.querySelector('.box').scrollTop: 스크롤바를 위에서 부터 얼마나 내렸는지
* document.querySelector('.box').scrollHeight: 스크롤 시키지 않았을때 창 전체 높이
* document.querySelector('.box').clientHeight: 눈에 보이는 많큼의 창 높이

 ```js
 //박스 끝까지 스크롤시 알림띄우기

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

## 11. 이벤트 버블링
이벤트 버블링은 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성을 의미한다.

### 1. 이벤트 버블링 관련 함수

 ```js
document.querySelector('.black-bg').addEventListener('click', function(e){
  e.target;  //실제 클릭한 요소 알려줌
  e.currentTarget;  //지금 이벤트리스너가 달린 곳 알려줌
  e.preventDefault();  // 실행하면 이벤트 기본 동작을 막아줌
  e.stopPropagation();   //실행하면 내 상위요소로의 이벤트 버블링을 중단해줌
}) 
//파라미터는 아무거나 넣어도 되지만, 통상적으로 e를 사용
 ```
### 2. 이벤트 버블링 에러 해결
지금 실제로 클릭한 것이 검은 배경일 때만 닫으라는 조건을 추가
 ```js
 $('.black-bg').on('click', function(e){
    if(e.target == document.querySelector('.black-bg')) {
        $('.black-bg').removeClass('show-modal');
        }
    })
    
//jQuery
$('.black-bg').on('click', function(e){
    if($(e.target).is($('.black-bg'))) {
            $('.black-bg').removeClass('show-modal');
        }
    });
```
 <br>

## 12. 탭 만들기
탭 UI는 여러 문서, 패널을 하나의 창에 두고 전환하여 볼 수 있도록 구현한 인터페이스를 뜻한다.
1. tab 디자인
2. js로 버튼누르면 창 전환하도록 작성

* dataset 사용               
dataset: 데이터 속성은 HTML 요소의 'data-' 로 시작하는 속성이다. 이러한 데이터 속성은 특정한 데이터를 DOM 요소에 저장해두기 위함이 목적이다. 문법:<div data-데이터이름="값">
 ```js
<ul class="list">
<li class="tab-button" data-id="0">Products</li>
<li class="tab-button" data-id="1">Information</li>
<li class="tab-button" data-id="2">Shipping</li>
</ul>

//버튼을 클릭하면 해당 버튼의 아이디를 함수의 파라미터로 전달
$('.list').click(function(e){
  openTab(e.target.dataset.id) 
  //dataset 가져오는 법: document.querySelector().dataset.데이터이름
}
  function openTab(n){
    $('.tab-button').removeClass('orange');  //모든 탭에서 orange class 삭제
    $('.tab-button').eq(n).addClass('orange');  //해당 tab에 orange class 추가
    $('.tab-content').removeClass('show');  //모든 탭에서 show class 삭제
    $('.tab-content').eq(n).addClass('show');  //해당 tab에 show class 추가
} 
 ```

 <br>

## 13.셀렉트 박스
사용자가 다양한 선택지 중에서 선택을 하는 드롭박스를 만드는 태그

1. 셀렉트 박스 디자인
2. 옵션 선택시 하위 옵션 추가       

* js로 html 생성하는 방법

```html
<div id="test">
</div>

<script>
  var a = '<p>안녕</p>';
  $('#test').append(a);
  
//추가가 아니라 아예 바꾸고 싶은 경우
  $('#test').html(a);
</script>
```

```js
  var pants = [28, 30, 32];
  var shirts = [105, 100, 95]

  $('.form-select').eq(0).on('change', function(){
    var value = this.value;

    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
      $('.form-select').eq(1).html(''); 
      shirts.forEach(function(data){
        $('.form-select').eq(1).append('<option>'+data+'</option>'); 
    })
  }
    else if(value == '바지'){
      $('.form-select').eq(1).removeClass('form-hide');
      $('.form-select').eq(1).html('');
      pants.forEach(function(data){
        $('.form-select').eq(1).append('<option>'+data+'</option>');
      })
    }
    else 
    $('.form-select').eq(1).addClass('form-hide');
    })
```

 <br>

## 14. Ajax 요청
서버에 GET, POST 요청을 할 때 새로고침 없이 데이터를 주고받을 수 있게 도와주는 간단한 브라우저 기능

### 1. jQuery로 AJAX요청하기
1) get
```js
//https://codingapple1.github.io/hello.txt에서 데이터를 받아온 후 출력하기
$.get('https://codingapple1.github.io/hello.txt').done(function(data){
  console.log(data)
})
```
2) post
```js
//https://codingapple1.github.io/hello.txt에 {name : 'kim'} 데이터 전송하기
$.post('https://codingapple1.github.io/hello.txt', {name : 'kim'})
```
### 2. Ajax를 사용하여 상품 더보기 버튼 만들기
```js
 $('#more').click(function(){ //더보기 클릭 이벤트 발생
    number++;  
    if(number==1){ //한 번 눌렀을 경우
    //첫 번째 URL에서 데이터를 가져와 카드 레이아웃 생성 함수로 전달
      $.get('https://codingapple1.github.io/js/more1.json').done(function(products2){
        showProucts(products2);  //카드 레이아웃 생성
    })}
    else if(number==2){
      //두 번째 URL에서 데이터를 가져와 카드 레이아웃 생성 함수로 전달
      $.get('https://codingapple1.github.io/js/more2.json').done(function(products3){
        showProucts(products3);  //카드 레이아웃 생성
        $('#more').css('display', 'none')  //더보기 버튼 없애기
    })}
 })
```

 <br>

## 15. array 정렬 함수

 ### 1. sort
배열의 요소를 오름차순 또는 내림차순으로 정렬
#### 1. 숫자 오름차순
```js
var arr=[30,5,2,47,15]
arr.sort(function(a,b){
    return a-b;
});
//a-b가 양수일 경우 a를 오른쪽으로
//a-b가 음수일 경우 b를 오른쪽으로
```
#### 2. 숫자 내림차순
```js
arr=[30,5,2,47,15]
arr.sort(function(a,b){
    return b-a;
});
//b-a가 양수일 경우 a를 오른쪽으로
//b-a가 음수일 경우 b를 오른쪽으로
```
#### 3. 문자 오름차순
```js
var arr=['나','라','가','다']
arr.sort();
```
#### 4. 문자 내림차순
```js
var arr=['나','라','가','다']
arr.sort(function (a, b) {
    if (a > b) return -1;
    else if (b > a) return 1;
    else return 0;
  });
//a>b일 경우 b가 오른쪽으로
//b>a일 경우 a가 오른쪽으로
```
<br>

### 2. filter
주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
```js
var arr = [7,3,5,2,40];

var arr2 =arr.filter(function(a){
  return a < 4
}); 
```
<br>

### 3. map
array 안의 자료들을 전부 변형할 때 사용
```js
var arr = [7,3,5,2,40];

var arr2 = arr. map(function(a){
  return a * 4
}); 
```

 <br>

## 16. DOM개념 정리
DOM: 자바스크립트가 HTML에 대한 정보들 (id, class, name, style, innerHTML 등)을 object 자료로 정리한 것

자바스크립트는 html에 특화된 언어이지만, html 문법을 직접 해석하고 조작할 수 없다. 따라서 자바스크립트가 HTML 조작을 하기 위해선 HTML을 자바스크립트가 해석할 수 있는 문법으로 변환해놓아야 한다.

브라우저는 HTML문서를 위에서 부터 차례로 읽어내려간다. 읽을 때 마다 HTML을 발견하면 DOM에 추가해준다.


 <br>

## 17. 로컬스토리지
로컬스토리지는 브라우저 저장공간으로, key-value 형태로 문자, 숫자 데이터 저장가능, 브라우저를 재접속해도 남아있다.

### 1. 로컬스토리지 사용법
```js
localStorage.setItem('이름', 'kim') //자료저장하는법
localStorage.getItem('이름') //자료꺼내는법
localStorage.removeItem('이름') //자료삭제하는법
```

* 로컬스토리지에는 문자, 숫자만 저장이 가능하여 array, object 형태의 자료는 저장시 문자로 강제로 변환되어 형태가 깨지게 된다. 따라서 array, object 형태로 데이터를 저장하고 싶을 때는 JSON 형식으로 바꿔서 저장한 후 다시 꺼낼 때는 array, object 형식으로 바꿔주면 된다.

array/object -> JSON 변환하고 싶으면 JSON.stringify()              
JSON -> array/object 변환하고 싶으면 JSON.parse()

 ```js
var arr=[1,2,3]; 
var newArr=JSON.stringify(arr);  //arr을 JSON형식으로 저장
localStorage.setItem('num',newArr); //newArr를 로컬스토리지에 저장
var reArr=JSON.parse(newArr); //JSON을 arr형식으로 변환
console.log(reArr); //출력하면 원래 array 형식대로 출력됨
```
<br>

### 2. 장바구니 기능 만들기
구매를 클릭하면 해당 상품명이 로컬스토리지에 배열의 형태로 저장됨
```html
<script>
    $('.buy').click(function(){
        
        var item=$(this).siblings('h5').text(); 
        //클릭한 노드의 형제 노드 중 h5에 해당하는 텍스트 즉, 해당 상품명을 변수에 저장
        if(localStorage.getItem("cart") == null){
        //key가 cart인 데이터가 로컬스토리지에 없을 경우
            localStorage.setItem('cart', JSON.stringify([item]));
            //배열에 해당 상품명을 담아 JSON으로 변환하여 로컬스토리지에 저장
        }
        else{ //key가 cart인 데이터가 로컬스토리지에 있을 경우
            var itemArr=JSON.parse(localStorage.cart); 
            //해당 데이터를 가져와서 배열의 형태로 변환하여 저장
            itemArr.push(item); 
            //해당 상품명을 배열에 추가
            localStorage.setItem('cart', JSON.stringify(itemArr)); 
            //배열을 다시 JSON으로 변환하여 로컬스토리지에 저장
        }
    })
 </script>
```