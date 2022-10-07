### 셀릭트 박스(HTML 내용추가, forEach)
> 사용자가 다양한 선택지 중에서 선택을 하는 드롭박스를 만드는 태그

<br>

### 1. 셀렉트 박스 형식                   
:option 태그 안에 옵션을 입력하여 생성

```html
<form class="container my-5 form-group">
    <p>상품선택</p> 
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>
```

<br>

### 2. 하드코딩으로 옵션 선택시 하위 옵션 추가
```html
//셔츠 클릭시 사이즈 선택 옵션 제공하기

<form class="container my-5 form-group">
    <p>상품선택</p> 
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>

    //셔츠 사이즈 데이터 하드 코딩
    <select class="form-select mt-2 form-hide">
      <option>105</option>
      <option>100</option>
      <option>95</option>
      <option>90</option>
    </select>
</form>

<style>
  form-hide {
    display:none;
  }
</style>

<script>
  $('.form-select').eq(0).on('change', function(){ //옵션을 선택하면

    var value = this.value;  //선택한 값 저장
    if (value == '셔츠') {  //선택한 값이 셔츠일 경우
       $('.form-select').eq(1).removeClass('form-hide'); //하위 옵션 보여주기
     }
    else 
    $('.form-select').eq(1).addClass('form-hide');
    })
</script>
```
※주의사항: '사용자가 옵션을 선택하면'($('.form-select').eq(0).on('change', function())을 입력하지 않을 경우: script 태그 안에 내용은 처음 페이지를 로드할 때 한 번 실행되고 끝나기 때문에 사용자가 옵션을 선택해도 아무런 동작이 실행되지 않는다.

<br>

### 3. js에서 html 내용을 생성하는 방식으로 하위 옵션 추가
html 안에 직접 데이터를 넣는 방식으로 하드코딩하면 확장성이 떨어진다. 따라서 js에서 html 내용을 생성하는 방식으로 옵션을 추가하는 방식으로 확장성을 높일 수 있다.

<br>

### 3-1. JS로 html 내용 생성하는 방법


#### 1.createElement()로 자료 생성 후 appendChild()로 추가
```html
<div id="test">
  
</div>

<script>
  var a = document.createElement('p');  //p태그를 생성해서 변수 a에 저장
  a.innerHTML = '안녕';
  document.querySelector('#test').appendChild(a); //a를 id가 test인 태그의 자식으로 추가
</script>
```
<br>

#### 2. html 문법대로 작성 후 insertAdjacentHTML()로 추가

```html
<div id="test">
  
</div>

<script>
  var a = '<p>html 추가</p>'; //html 문법 그대로 변수 a에 저장
  document.querySelector('#test').insertAdjacentHTML('beforeend', a); //id가 test인 태그의 맨 아래에 추가
</script>
```
* jQuery의 경우
```html
<div id="test">
  
</div>

<script>
  var a = '<p>안녕</p>';
  $('#test').append(a);
</script>
```

* 추가가 아니라 아예 바꾸고 싶은 경우
```js
  document.querySelector('#test').innerHTML('<p>html 추가</p>'); 

  $('#test').html('<p>html 추가</p>');
```

<br>

### 3-2. html내용 생성 문법 적용하여 하위 옵션 추가

```html
//셔츠를 클릭 시 셔츠 사이즈, 바지를 클릭 바지 사이즈 옵션 추가

<form class="container my-5 form-group">
    <p>상품선택</p> 
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>

    <select class="form-select mt-2 form-hide"></select>  //하위 옵션이 들어갈 자리
 
 <script>
  $('.form-select').eq(0).on('change', function(){
    var value = this.value;

    if (value == '셔츠') {
      var shirtsSize= '<option>100</option> <option>95</option>';  //html 문법대로 셔츠 사이즈 옵션 저장
      $('.form-select').eq(1).html(shirtsSize);  //셔츠 사이즈 옵션을 html에 생성
       $('.form-select').eq(1).removeClass('form-hide');  //옵션 보이기
     }

    else if(value == '바지'){
      var pantsSize= '<option>30</option> <option>28</option>';  //html 문법대로 바지 사이즈 옵션 저장
      $('.form-select').eq(1).html(pantsSize);  //바지 사이즈 옵션을 html에 생성
      $('.form-select').eq(1).removeClass('form-hide');  //옵션 보이기
    }
    
    else 
    $('.form-select').eq(1).addClass('form-hide');
    })
</script>
```
<br>

### 4. forEach 문법을 사용하여 외부에서 데이터를 받아서 하위 옵션 추가 
3.에서 js로 html 내용을 추가하는 방법으로 확장성을 높이긴 했지만, 어쨌든 위에서는 js에서 데이터를 하드코딩하였다. 따라서 받은 데이터를 forEach 반복문을 사용하여, 동적으로 옵션을 생성하면 더 확장성을 높일 수 있다.

### 4-1 다양한 반복문
#### 1. forEach
:배열을 순회하기 위해 사용한다.

```js
var array = [a, b, c, d];
array.forEach(function(data, i){
  console.log(data, i)
});
```
* forEach문을 사용할 때는 무조건 콜백 함수를 입력해야 한다.
* forEach문 안에 있는 코드는 배열 원소의 개수만큼 반복된다.
* 첫 번째 파라미터인 data는 배열의 원소를 저장한다.
* 첫 번째 파라미터인 i는 배열의 인덱스를 저장한다.

<br>

#### 2. for in
:객체를 순회하기 위해 사용한다.
```js
var obj = { name : 'kim', age : 20 }

for (var key in obj){
  console.log(key, obj[k])
}
```
* for-in문 안에 있는 코드는 객체 데이터의 개수만큼 반복된다.
* 변수 key에는 객체의 key를 저장한다.
* 따라서 obj[key]는 객체의 value값을 말한다.

<br>

### 4-2. for-in 반복문 적용하여 하위 옵션 추가
```js
  var pants = [28, 30, 32];
  var shirts = [105, 100, 95]

  $('.form-select').eq(0).on('change', function(){
    var value = this.value;

    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
      $('.form-select').eq(1).html(''); 
      //하위 옵션의 html 내용 초기화 (초기화 하지 않으면 클릭할 때 마다 하위옵션이 계속 추가됨)
      shirts.forEach(function(data){
        $('.form-select').eq(1).append('<option>'+data+'</option>'); //
      //array에 저장된 데이터를 순서대로 옵션으로 저장
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