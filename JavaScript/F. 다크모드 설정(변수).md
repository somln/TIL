# 다크모드 설정하기(변수)
>변수를 사용하여 다크 모드 버튼을 만들 수 있다.

 <br>

### 1. 다크모드 버튼 생성하기
```html
<span class="badge bg-dark">Dark 🔄</span>
```

<br>

### 2. 다크모드 클래스 만들기
```css
.dark{
  background-color: black;
  color:white;
}
```

<br>

### 3. 변수를 사용하여 토글
```html
 <script>
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
  </script>
```
<br>

---------------------

<br>


## 변수 생성 문법

|var|let|const|
|:---:|:---:|:---:|
|Function|{}|{}|
|재선언O|재선언X|재선언X|
|재할당O|재할당O|재할당X|
