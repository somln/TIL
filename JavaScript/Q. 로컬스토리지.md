# 로컬스토리지

### 1. 브라우저 저장 공간
* Local Storage:  key-value 형태로 문자, 숫자 데이터 저장가능, 브라우저를 재접속해도 남아있음
* Session Storage: key-value 형태로 문자, 숫자 데이터 저장가능, 브라우저를 재접속 하면 날라감
* Indexed DB:크고 많은 구조화된 데이터를 DB처럼 저장가능
* Cookies: 유저 로그인정보 저장공간
* Cache Storage: html css js img 파일 저장해두는 공간

<br>

### 2. 로컬스토리지 사용법
```js
localStorage.setItem('이름', 'kim') //자료저장하는법
localStorage.getItem('이름') //자료꺼내는법
localStorage.removeItem('이름') //자료삭제하는법
```

<br>

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

* 로컬스토리지에 저장된 자료를 수정할 수 있는 방법은 없기 때문에 다음과 같이 코드를 작성해야 한다.
1. 수정하려는 자료 꺼내기
2. 꺼낸 데이터를 수정하기
3. 데이터를 다시 넣기

<br>

### 3. 장바구니 기능 만들기
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
<br>
update: 같은 상품은 중복으로 추가되지 않게 설정 

```html
<script>
    $('.buy').click(function(){
        var item=$(this).siblings('h5').text();
        if(localStorage.getItem("cart") == null){
            localStorage.setItem('cart', JSON.stringify([item]));
        }
        else{
            var itemArr=JSON.parse(localStorage.cart);
            if (itemArr.includes(item)){
                alert('이미 추가한 상품입니다');
            }
            else{
                itemArr.push(item);
                localStorage.setItem('cart', JSON.stringify(itemArr));
            }
        }
    })
</script>
```
