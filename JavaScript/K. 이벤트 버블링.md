# 이벤트 버블링
>이벤트 버블링은 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성을 의미한다.

<br>

### 1. 이벤트 버블링 발생     

```html 
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
```

<img width="958" alt="image" src="https://user-images.githubusercontent.com/92261242/194243792-c80b0956-e343-47d1-9c16-09214010d416.png">


<br>

위 화면에서 검은색 배경을 눌렀을 때 로그인 창이 닫히도록 작성할 때, 아래와 같이 작성하면 버그가 발생하는 이유: 

```js  
    $('.black-bg').on('click', function(){
        $('.black-bg').removeClass('show-modal');
    });
```
검은 배경을 눌렀을 때 로그인 창이 닫히는 것은 맞게 작동하지만, 흰배경, input, 글자 등 모달창 내부의 어떤 것을 눌러도 로그인창이 닫힌다. 그 이유는 유저가 "white-bg"나 "form-control" 등 다른 곳을 클릭해도 이벤트 버블링 때문에 상위 태그인 "black-bg"도 클릭한 것으로 되고, 따라서 이벤트리스너가 동작해서 모달창이 닫히게 된다.<br>             
따라서 위와 같은 버그를 해결하기 위해서는 위 코드에서 지금 실제로 클릭한 것이 검은 배경일 때만 닫으라는 조건을 추가해야한다.


<br>

### 2. 이벤트 버블링 관련 함수

```js
document.querySelector('.black-bg').addEventListener('click', function(e){
  e.target;  //실제 클릭한 요소 알려줌
  e.currentTarget;  //지금 이벤트리스너가 달린 곳 알려줌
  e.preventDefault();  // 실행하면 이벤트 기본 동작을 막아줌
  e.stopPropagation();   //실행하면 내 상위요소로의 이벤트 버블링을 중단해줌
}) 
//파라미터는 아무거나 넣어도 되지만, 통상적으로 e를 사용
```

<br>

### 3. 이벤트 버블링 해결

```js
 $('.black-bg').on('click', function(e){
    //지금 실제로 클릭한 것이 검은 배경일 때만 닫으라는 조건을 추가
        if(e.target == document.querySelector('.black-bg')) {
            $('.black-bg').removeClass('show-modal');
        }
    });
```
<br>

jquery의 경우
```js
 $('.black-bg').on('click', function(e){
        if($(e.target).is($('.black-bg'))) {
             $('.black-bg').removeClass('show-modal');
        }
    });
```
