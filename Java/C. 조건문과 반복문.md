# 조건문과 반복문

## 1. 조건문
### 1) if~ else if~else
```java
if(조건식 1){ 
    수행문 1 //조건식 1이 참이면 수행       
}
else if(조건식 2){
    수행문 2  //조건식 1이 거짓이고 2가 참이면 수행
}
else if(조건식 3){
    수행문 3 //조건식 1,2가 거짓이고 3이 참이면 수행
}
else{
    수행문 4 //조건식 1,2,3 모두 거짓이면 수행
}
```
* if~else: 위에 조건이 참이면 더 코드를 실행하지 않음.
* if, if: 조건이 나올  떄 마다 계속 코드를 실행함

<br>

### 조건문과 조건 연산자
```java	
//조건문
	if(a>b)
		max=a;
	else 
		max=b;

//조건 연산자
	max=(a>b) ? a : b;
 ```
<br>

### 2) switch-case 문
* 조건의 값이 하나의 숫자/ 문자. 문자열 로 표현될 수 있는 경우 간단하게 구현될 수 있다.
```java	
int ranking = 1;
char medalColor;
	
	switch(ranking){ 
		
		case 1: medalColor = 'G';   //ranking에 저장된 값이 1일 경우실행
			break;
		
		case 2: medalColor = 'S';  //ranking에 저장된 값이 2일 경우실행
			break;
			
		case 3: medalColor = 'B';  //ranking에 저장된 값이 3일 경우실행
			break;
		default:
			    medalColor = 'A';  //위 케이스를 모두 만족하지 않는 경우 실행
```
* break를 입력하지 않으면 break를 만날 때 까지 아래 코드를 실행하기 때문에, 조건 1게마다 braek를 적어줘야 한다.

<br>

### case문 동시에 사용하기
```java	
int month = 10;
	int day;
		
	switch(month){
		
		case 1: case 3: case 5: case 7: case 8: case 10: case 12:
			day = 31;
			break;

		case 4: case 6: case 9: case 11:
			day = 30;
			break;
		case 2: 
			day = 28;
			break;
		default:
			day = 0;
		    System.out.println("존재하지 않는 달 입니다.")
```

<br>

## 2. 반복문

### 1) whlie
조건식이 참일 때 까지 괄호 안 수행문 실행
```java
초기화식
while(조건식){
	//수행문
	......
	증감식
}
```
```java
int num=1;
int sum=0

while(num<=10){
	sum+=num;
	num++;
}
```

<br>

### 2) do~while
수행문을 무조건 1번은 실행한 뒤에 조건식이 참이면 do안의 수행문 실행
```java
초기화식 
do{
	//수행문
	증감식
}while(조건식);
```
```java
int num=1;
int sum=0
do{
	sum+=num;
	num++;
}
while(num<=10);
```
<br>

### 3) for
조건식이 참이 때 까지 괄호 안 수행문 실행

```java
for(초기화식; 조건식; 증감식){
	//수행문
}
```
```java
int sum=0;
for(int num=1; num<10; num++){
	sum+=num;
}
```

### 4) 중첩 반복문
```java
int dan;
int times;
		
	for(dan = 2; dan <=9; dan++){
		for(times = 1; times <=9; times++){
			System.out.println(dan + "X" + times + "=" + dan * times);
		}
		System.out.println();
	}
```
<br>

### 5) continue 문
반복문과 함께 쓰이며, 반목문 내부 continue문을 만나면 이후 반복되는 부분을 수행하지 않고 조건식이나 증감식을 수행한다.
```java
// 1 부터 100까지 홀수만 더하는 코드
int total=0;
int num=0;

for(num=1; num<100; num++){
	if(num%2==0){
		continue;
	}
	total+=num;
}
```
<br>

### 6) break문
반복문에서 break 문을 만나면 더 이상 반복을 수행하지 않고 반복문을 빠져나온다. 중첩된 반복문에서는 가장 가까운 반복문 하나만 빠져나온다.
```java
//sum이 100 초과가 되면 반복문 종료
int sum=0;
int num=1;

while(true){
	sum+=num;
	if(sum>100)
	   break;
	num++;   
}
System.out.println(sum); //105
System.out.println(num);  //14
```