# array 정렬 함수

### 1. sort
>배열의 요소를 오름차순 또는 내림차순으로 정렬\
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
> 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
```js
var arr = [7,3,5,2,40];

var arr2 =arr.filter(function(a){
  return a < 4
}); 
```
<br>

### 3. map
>array 안의 자료들을 전부 변형할 때 사용
```js
var arr = [7,3,5,2,40];

var arr2 = arr. map(function(a){
  return a * 4
}); 
```
<br>

### 4. 응용하기
1. "가격 오름차순" 버튼과 기능 만들기
2. "상품명 다나가순 정렬" 버튼과 기능을 만들기
3. "6만원 이하 상품보기" 버튼과 기능을 만들기

<img width="879" alt="image" src="https://user-images.githubusercontent.com/92261242/195321067-a3b3593a-2ea9-4c55-93a5-b606958b7988.png">

```html
<div class="container">
      <button class="btn btn-danger btn-sort">낮은 가격순</button>
      <button class="btn btn-danger btn-sort">상품명 내림차순</button>
      <button class="btn btn-danger btn-sort">6만원 이하</button>
      </div>

<script>
 $('.btn-sort').eq(0).click(function(){ //낮은 가격순 버튼 클릭
        products.sort(function(a,b){  //낮은 가격순으로 정렬
            return a.price-b.price
        })
        $('.row').html('')  //'.row'의 html 비우기
        showProucts(products)  //카드레이아웃 출력 함수로 전달
    })

    $('.btn-sort').eq(1).click(function(){  //상품명 내림차순 버튼 클릭
        products.sort(function(a,b){  //상품명 내림차순으로 정렬
            if (a.title > b.title) return -1;
            else if (b.title > a.title) return 1;
            else return 0;
        })
        $('.row').html('')
        showProucts(products)
    })

    $('.btn-sort').eq(2).click(function(){  //6만원 이하 버튼 클릭
        var new_products=products.filter(function(a){  //6만원 이하로 정렬
            return a.price<=60000
        })
        $('.row').html('')
        showProucts(new_products)
    })

</script>
```
