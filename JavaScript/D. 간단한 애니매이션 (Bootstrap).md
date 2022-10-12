# 간단한 애니매이션 만들기
> one-way 애니매이션: A상태에서 B상태로 움직인는 애니매이션     

<br>

### [ one-way 일방향 애니메이션 만드는 법 ]

1. 시작스타일 만들기 (class로)
```css

.black-bg {
    width : 100%;
    height : 100%;
    position : fixed;
    background : rgba(0,0,0,0.5);
    z-index : 5;
    padding: 30px;
    visibility: hidden;
    opacity: 0;
  }

```

2. 최종스타일 만들기 (class로) 
```css
  .show-modal {
    visibility: visible;
    opacity: 1;
  }
  
```

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
<br>

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
