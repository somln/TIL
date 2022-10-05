# 타이머 기능

>어떤 코드를 바로 실행하지 않고 일정 시간 기다린 후 실행해야하는 경우, 혹은 일정 시간마다 코드를 반복해야하는 경우 타이머기능을 사용한다.           

<br>

 타이머 함수
* setTimeout & clearTimeout
* setInterval & clearInterval

<br>

### 1. setTimeout & clearTimeout       
:일정 시간 후에 특정 코드, 함수를 의도적으로 지연한 뒤 실행하고 싶을 때 사용하는 함수이다.

```js
let timer = setTimeout(function(){ }, delay);

//setTimeout 을 지연시간 기다리지 않고 종료시키기
clearTimeout(timer);
```
<br>

### 2. setInterval & clearInterval:              
:일정 시간을 간격으로 콜백함수를 반복 호출 하는 함수이다.

```js
let interval = setInterval(function(){ }, delay);

//setInterval을 지연시간 기다리지 않고 종료시키기
clearInterval(interval);
```

<br>

### 3. 사용 예시    
"5초 이내 구매시 사은품 증정" 이라는 문자를 1초마다 5에서 1씩 감소시킨 후, 0이 되면 문자가 보이지 않도록 처리하기.   

```html
<div class="alert alert-danger">
  <span id="num">5</span>초 이내 구매시 사은품 증정
</div>
  ```

```js
 <script>
      var count = 5;
      setInterval(function(){
        count -= 1;
        if (count >= 0){
            $('#num').html(count);
        }
        else{
            $('.alert').hide();
        }
    }, 1000);
  </script>
```