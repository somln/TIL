# 변수와 자료형

## 1. bit 단위
### 1) 진법
* 2진수: 숫자 앞에 0B 입력
* 8진수: 숫자 앞에 0 입력
* 16진수: 숫자 앞에 0X 입력

```java
	public static void main(String[] args) {

		int num=10;
		int bNum=0B1010;  //2진수
		int oNum=012; //8진수
		int hNum=0XA; //16진수
		
		System.out.println(num);
		System.out.println(bNum);
		System.out.println(oNum);
		System.out.println(hNum);
		// 모두 다 10으로 출력됨
	}
```

<br>

### 2) 음의 정수 표현
### 정수의 가장 왼쪽에 존재하는 비트는 부호 비트
* 0: 양수
* 1: 음수 

### 양수->음수 만드는 방법:  2의 보수 만들기
1. 1의 보수를 취한다
2. 1을 더한다. 

ex) 5 -> -5               
00000101 -> 11111010 -> 11111011

음수의 경우는 2의 보수를 취해야 그 수가 실제 얼마인지 알 수 있다.  
 
 <br>

## 2. 변수
### 1) 선언, 초기화
```java
	int num;  //선언
	num=10;  //초기화
	int level=20;  //선언과 동시에 초기화
```
<br>

### 2) 자료형
* byte: 1바이트 단위
* short: 2바이트 단위
* char: 2바이트, 문자형
* int: 4바이트, 정수형
* long: 8바이트, 정수형,     
정수는 기본적으로 int(4바이트)로 저장-> 숫자 뒤에 l 또는 L을 입력해야함
* float: 4바이트, 실수 자료형          
실수는 기본적으로 double(8바이트)로 저장-> 숫자 뒤에 f 또는 F를 입력해야함
* double: 8바이트, 실수 자료형
* boolean: true for flase 저장

문자는 내부적으로 정수형으로 표현 된다
```java
	char ch='A';
	System.out.println(ch);  //A 출력
	System.out.println((int)ch);  //65 출력
	
	ch=66;
	System.out.println(ch); //B 출력
    		
	int ch2=67;
	System.out.println((char)ch2); //C 출력
```

<br>

### 3) 상수와 리터럴
상수: 변하지 않는 값            
선언 방법: final 키워드 사용
```java
final int MAX_NUM=100;
final float PI=3.14F;
```
위 코드에서 100, 3.14와 같은 값을 '리터럴'이라고 한다. 리터럴에 해당되는 값은 특정 메모리 공간인 상수풀에 저장되고 필요한 경우 가져와 사용하게 된다.

<br>

### 4) 형 변환
1. 묵시적 형변환: 컴파일러에 의해 자동으로 형변환
* 좁은 데이터 타입 -> 넓은 데이터 타입 ex) int -> double
* 덜 정밀한 수 -> 더 정밀한 수 ex) int -> float
```java
	//좁은 데이터 타입 -> 넓은 데이터 타입
	byte bNum=10;
	int num=bNum;
	System.out.println(num);
		
	//덜 정밀한 수 -> 더 정밀한 수
	long lNum=10;
	float fNum=lNum;
	System.out.println(fNum);
		
	// num(int)+ fNum(float) -> float
	// float -> double
	double dNum=fNum+num;
	System.out.println(dNum);
```
2. 명시적 형변환: 사용자가 직접 데이터 타입을 변경하는 것
변환이 이루어지는 과정에서 자료의 손실이 발생할 수 있다.

```java
    int iNum=1000;
	//byte bNum=iNum; 오류 발생
	byte bNum=(byte)iNum;
	System.out.println(bNum); //-24 출력, 데이터 유실 발생
		
	double dNum=3.14;
	iNum=(int)dNum;
	System.out.println(iNum);  //3 출력, 데이터 유실 발생
		
	float fNum=0.9F;
	int num1=(int)dNum+(int)fNum;
	int num2=(int)(dNum + fNum); 
		
	System.out.println(num1); //3
	System.out.println(num2); //4

```
