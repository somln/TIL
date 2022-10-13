# Ajax 통신

### 1. 서버와 요청에 대한 용어 정리
#### 1. 서버란?
> 클라이언트의 요청을 받으면 서비스, 데이터를 제공하는 컴퓨터 혹은 프로그램


서버에 데이터를 요청할 때는

1. 어떤 데이터인지 url로 기재해

2. 어떤 방법으로 요청할지 결정( GET/POST 등)

하면 데이터를 보내준다.

<br>

#### 2. GET, POST
1) GET
>클라이언트에서 서버로 어떠한 리소스로 부터 정보를 요청하기 위해 사용되는 메서드                

요청 방법: 브라우저 주소창에 url 적으면 그 곳으로 GET요청된다.


2) POST
>리소스를 생성/업데이트하기 위해 서버에 데이터를 보내는 데 사용 

 요청 방법: form 태그를이용하면 폼이 전송되었을 때 POST요청을 날려준다.
```html
<form action="요청할url" method="post">
```

<br>

#### 3. Ajax란?
>서버에 GET, POST 요청을 할 때 새로고침 없이 데이터를 주고받을 수 있게 도와주는 간단한 브라우저 기능

기본적으로 HTTP 프로토콜은 클라이언트쪽에서 Request를 보내고 서버쪽에서 Response를 받으면 이어졌던 연결이 끊기게 되어있다. 그래서 화면의 내용을 갱신하기 위해서는 다시 request를 하고 response를 하며 페이지 전체를 갱신하게 된다. 하지만 이렇게 할 경우, 엄청난 자원낭비와 시간낭비를 초래하고 말 것이다.

AJAX는 HTML 페이지 전체가 아닌 일부분만 갱신할 수 있도록 XMLHttpRequest객체를 통해 서버에 request한다. 이 경우, JSON이나 XML형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있다.

<br>

### 2. jQuery로 AJAX요청하기 
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

3) Ajax 요청 실패시
```js
$.get('https://codingapple1.github.io/hello.txt')
  .done(function(data){
    console.log(data)
  })
  .fail(function(error){
    console.log('실패함')
  });
```

4) JSON이란?        
>데이터를 쉽게 ' 교환 ' 하고 ' 저장 ' 하기 위한 텍스트 기반의 데이터 교환 표준    

서버와 데이터를 주고받을 때는 문자만 주고받을 수 있다. 따라서 array, object 는 전송이 불가능하기 때문에 object를 JSON으로 바꿔서 전송해야한다. array 아니면 object에 따옴표를 쳐서 '{ "price" : 5000 }' 이렇게 만들면 JSON이라는 자료가 된다. JSON은 문자로 인식하기 때문에 서버와 데이터주고받기가 가능하다. jQuery의 $.get()는 JSON으로 자료가 도착하면 알아서 array/object 자료로 바꿔주기 때문에 편리하다.

<br>

### 3. Ajax를 사용하여 상품 더보기 버튼 만들기
1. 기본 상품 카드 레이아웃 출력하기
2. 더보기 버튼을 하나 만들기
3. 해당 버튼을 누르면 첫 번째 URL로 GET요청하여 상품 3개 데이터를 받아오기
4. 받아온 데이터로 카드 레이아웃 3개 더 만들기
5. 더보기 버튼 한번 더 누르면 두 번째 URL로 GET요청하여 상품 3개 데이터를 더 받아오기
6. 받아온 데이터로 카드 레이아웃 3개 더 만들기
7. 더 이상의 데이터가 없으므로 더보기 버튼 삭제하기

<img width="907" alt="image" src="https://user-images.githubusercontent.com/92261242/195267807-8ee5a3af-9ee5-47e2-854b-28d3f861a379.png">


```js
//더보기 버튼 생성
<div class="container">
<button class="btn btn-danger" id="more">더보기</button>
</div>

//기본 상품 데이터
var products = [
      { id : 0, price : 70000, title : 'Blossom Dress' },
      { id : 1, price : 50000, title : 'Springfield Shirt' },
      { id : 2, price : 60000, title : 'Black Monastery' }
    ];

showProucts(products); //기본 카드 레이아웃 출력

var number=0; //더보기를 누른 횟수 저장하는 변수

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

function showProucts(prod){ //함수에 상품 데이터 전달
 prod.forEach(function(data){ //데이터가 배열이므로 forEach 사용
                              //data는 배열의 요소인 객체 하나 하나를 의미
//append를 사용하여 js로 html 생성
 temp=`<div class="col-sm-4"> 
      <img src="https://via.placeholder.com/600" class="w-100">
      <h5>${data.title}</h5>
      <p>가격 : ${data.price}</p>
      </div>`

 $('.row').append(temp);
})
```



