# tab 만들기 (for 반복문)
>탭은 메인영역, aside 영역에 많이 사용되는 UI요소이다. 탭 UI는 여러 문서, 패널을 하나의 창에 두고 전환하여 볼 수 있도록 구현한 인터페이스를 뜻한다.

<br>

### 1.tab 디자인
```html
<div class="container mt-5">
        <ul class="list">
          <li class="tab-button">Products</li>
          <li class="tab-button">Information</li>
          <li class="tab-button">Shipping</li>
        </ul>
        <div class="tab-content">
          <p>상품설명입니다. Product</p>
        </div>
        <div class="tab-content">
          <p>스펙설명입니다. Information</p>
        </div>
        <div class="tab-content">
          <p>배송정보입니다. Shipping</p>
        </div>
      </div> 
```

```css
ul.list {
    list-style-type: none;
    margin: 0;
    padding: 0;
    border-bottom: 1px solid #ccc;
  }
  ul.list::after {
    content: '';
    display: block;
    clear: both;
  }
  .tab-button {
    display: block;
    padding: 10px 20px 10px 20px;
    float: left;
    margin-right: -1px;
    margin-bottom: -1px;
    color: grey;
    text-decoration: none;
    cursor: pointer;
  }
  .orange {
    border-top: 2px solid orange;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid white;
    border-left: 1px solid #ccc;
    color: black;
    margin-top: -2px;
  }
  .tab-content {
    display: none;
    padding: 10px;
  }
  .show {
    display: block;
  }

```

### 2. js로 버튼 누르면 클래스 추가
#### 버튼0 누르면

- 버튼0,1,2에 붙어있던 orange 클래스명 전부 제거하라고 코드 3줄 짜기

- 버튼0에 orange 클래스명 부착

- 박스0,1,2에 붙어있던 show 클래스명 전부 제거하라고 코드 3줄 짜기

- 박스0에 show 클래스명 부착

-> 버튼 1,2도 마찬가지

<br>

### 1) 정리되지 않은 코드

```js
$('.tab-button').eq(0).on('click', function(){
        $('.tab-button').removeClass('orange');
        $('.tab-button').eq(0).addClass('orange');
        $('.tab-content').removeClass('show');
        $('.tab-content').eq(0).addClass('show');
      });

$('.tab-button').eq(1).on('click', function(){
        $('.tab-button').removeClass('orange');
        $('.tab-button').eq(1).addClass('orange');
        $('.tab-content').removeClass('show');
        $('.tab-content').eq(1).addClass('show');
      })

$('.tab-button').eq(2).on('click', function(){
        $('.tab-button').removeClass('orange');
        $('.tab-button').eq(2).addClass('orange');
        $('.tab-content').removeClass('show');
        $('.tab-content').eq(2).addClass('show');
      })            
```

<br>

### 2) 반복문 사용
```js

var n = $( '.tab-content' ).length;

for(let i=0; i<n; i++){
        $('.tab-button').eq(i).on('click',function(){
          openTab(i)
        })
      }

      function openTab(n){
        $('.tab-button').removeClass('orange');
        $('.tab-button').eq(n).addClass('orange');
        $('.tab-content').removeClass('show');
        $('.tab-content').eq(n).addClass('show');
      } 
```
-> 반복문을 사용하면 코드의 반복을 줄일 수 있다.           
-> for 문 안에는 var 변수가 아닌 let 변수를 사용한다.

<br>

### 3) 이벤트 버블링 사용
이벤트 버블링을 활용하면 이벤트 리스너를 3개에서 1개로 줄일 수 있다.

```js
for(let i=0; i<3; i++){
        $('.list').click(function(e){
          if($(e.target).is($('.tab-button').eq(i))){
            openTab(i)
          }
        }
     )};
```
list 요소가 버튼1,2,3의 상위 요소이기 때문에 어떤 버튼을 클릭해도 list도 같이 클릭한 것으로 된다. 따라서 이벤트 리스너를 한 번만 사용한 후, 클릭한 버튼이 몇 번째 버튼인지 확인하는 코드를 넣으면 이벤트 리스너의 개수를 줄일 수 있다.
따라서, 버튼의 개수가 훨씬 더 많을 경우 이벤트리스너를 줄이면 램용량을 절약할 수 있다.

<br>

### 4) dataset 사용

>dataset: 데이터 속성은 HTML 요소의 'data-' 로 시작하는 속성이다. 이러한 데이터 속성은 특정한 데이터를 DOM 요소에 저장해두기 위함이 목적이다. 문법:<div data-데이터이름="값"></div> 

<br>

```html
<li class="tab-button" data-id="0">Products</li>
<li class="tab-button" data-id="1">Information</li>
<li class="tab-button" data-id="2">Shipping</li>
```

```js
//버튼을 클릭하면 해당 버튼의 아이디를 함수의 파라미터로 전달
$('.list').click(function(e){
  openTab(e.target.dataset.id) 
}
  //dataset 가져오는 법
  //document.querySelector().dataset.데이터이름
```