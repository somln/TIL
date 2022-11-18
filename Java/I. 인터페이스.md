# 인터페이스
## 1. 인터페이스란?
인터페이스는 클래스 혹은 프로그램이 제공하는 기능을 명시적으로 선언하는 역할을 한다. 추상 메서드와 상수로만 이루어져 있기 때문에 인스턴스를 생성할 수도 없다.    

Calc 인터페이스
```java
package interfaceex;

public interface Calc {  //interface로 선언
	
	//인터페이스에서 선언한 변수는 컴파일 과정에서 상수로 변환된다.
	//따라서 앞에 public static final을 붙인 것과 같다.
	
	double PI = 3.14;
	int ERROR = -9999999;
	
	//인터페이스에서 선언한 메서드는 컴파일 과정에서 추상 메서드로 변환된다. 
	//따라서 앞에 public abstarct를 붙이지 않아도 에러가 발생하지 않는다.
	int add(int num1, int num2);
	int substract(int num1, int num2);
	int times(int num1, int num2);
	int divide(int num1, int num2);
}
```

<br>

Calc 인터페이스를 Calculator 클래스에서 구현  //타입 상속
```java
package interfaceex;

public abstract class Calculator implements Calc{ 
    //구현 한다는 의미에서 implements 예약어 사용
    //추상 메서드를 2개만 구현하였으므로 추상 클래스

	@Override
	public int add(int num1, int num2) {
		return num1 + num2;
	}

	@Override
	public int substract(int num1, int num2) {
		return num1 - num2;
	}
}
```

<br>

Calculator 클래스를 상속받아 CompleteCalc 클래스 생성 //구현 상속
```java
package interfaceex;

public class CompleteCalc extends Calculator{
    //남은 추상 메서드 구현 -> 추상 클래스X

	@Override
	public int times(int num1, int num2) {
		
		return num1 * num2;
	}

	@Override
	public int divide(int num1, int num2) {
		if(num2 != 0 )
			return num1/num2;
		else 
			return Calc.ERROR;  //나누는 수가 0인 경우 오류 반환
	}
	
    //CompleteCalc에서 추가로 구현한 메서드
	public void showInfo(){
		System.out.println("Calc 인터페이스를 구현하였습니다" );
	}
}
```

<br>

CompleteCalc 클래스 실행해보기
```java
package interfaceex;

public class CalculatorTest {
	public static void main(String[] args) {
		int num1=10;
		int num2=5;
		
		Calc calc = new CompleteCalc();
		
		System.out.println(calc.add(num1, num2));
		System.out.println(calc.substract(num1, num2));
		System.out.println(calc.times(num1, num2));
		System.out.println(calc.divide(num1, num2));
		
		//calc.showinfo();는 불가능	
 	}
}
```
* 인터페이스를 구현한 클래스는 인터페이스 형으로 선언한 변수로 형 변환을 할 수 있음
* 상속에서 형 변환과 동일한 의미
* 단 클래스 상속과 달리 구현 코드가 없기 때문에 여러 인터페이스를 구현할 수 있음
* 형 변환시 사용할 수 있는 메서드는 인터페이스에 선언된 메서드만 사용할 수 있음

<br>

## 2. 인터페이스와 다형성

### 1) 인터페이스의 역할
클라이언트 프로그램에 어떤 메서드를 제공하는지 미리 알려주는 명세 또는 약속의 역할을 한다. 인터페이스에는 구현할 추상 메서드가 모두 선언되어 있고, 어떤 미개변수가 사용되는지, 어떤 자료형 값이 반환되는지 선언되어 있다. 따라서, 구현 객체를 직접 모르고 인터페이스 메서드만 알아도 객체 호출이 가능하게 한다.

<br>

### 2) 인터페이스와 다형성
인터페이스를 사용하면 다형성을 구현하여 확장성 있는 프로그램을 만들 수 있다. 즉, 클라이언트 프로그램을 많이 수정하지 않고 기능을 추가하거나 다른 기능을 사용할 수 있다.         
#### 예제 시나리오
고객센터에는 전화 상담원들이 있다. 고객센터로 전화가 오면 대기열에 저장된다. 상담원이 지정되기 전까지 대기상태가 됩니다.각 전화를 상담원에게 배분하는 정책은 다음과 같이 구현할 수 있다.

1. 순서대로 배분하기 : 모든 상담원이 동일하 상담건수를 처리하도록 들어오는 전화 순서대로 상담원에게 하나씩 배분한다.
2. 짧은 대기열 찾아 배분하기 : 고객 대기 시간을 줄이기 위해 상담을 하지 않는 상담원이나 가장 짧은 대기열을 보유한 상담원에게 배분한다.
3. 우선 순위에 따라 배분하기 : 고객 등급에 따라 등급이 높은 고객의 전화를 우선 가져와서 업무 능력이 좋은 상담원에게 우선 배분한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FCoeGE%2FbtrbpWZXvvs%2F02kkQK5BF21G12n0H4ATg0%2Fimg.png"> </img>

<br>

Scheduler 인터페이스 정의
```java
package scheduler;

public interface Scheduler {

	public void getNextCall();  //다음 전화를 가져오는 기능
	public void sendCallToAgent();  //상담원에게 전화를 배분하는 기능
	
}
```

<br>

순서대로 배분하기
```java
package scheduler;

//상담원 한명씩 돌아가며 동일하게 상담업무를 배분합니다.
public class RoundRobin implements Scheduler{

	@Override
	public void getNextCall() {
		System.out.println("상담 전화를 순서대로 대기열에서 가져옵니다");
		
	}

	@Override
	public void sendCallToAgent() {
		System.out.println("다음 순서 상담원에게 배분합니다.");
		
	}
}
```

<br>

짧은 대기열 먼저 배분하기
```java
package scheduler;

// 현재 상담업무가 없거나 상담대기가 가장 작은 상담원에게 배분합니다.
public class LeastJob implements Scheduler{

	@Override
	public void getNextCall() {
		System.out.println("상담 전화를 순서대로 대기열에서 가져옵니다");
		
	}

	@Override
	public void sendCallToAgent() {
		System.out.println("현재 상담업무가 없거나 상담대기가 가장 작은 상담원에게 할당합니다.");
		
	}

```

<br>

우선 순위에 따라 배분하기
```java
package scheduler;

// 고객등급이 높은 고객부터 대기열에서 가져와 업무 능력이 높은 상담원 우선으로 배분합니다.
public class PriorityAllocation implements Scheduler{

	@Override
	public void getNextCall() {
		System.out.println("고객 등급이 높은 고객의 전화를 먼저 가져옵니다.");
		
	}

	@Override
	public void sendCallToAgent() {
		System.out.println("업무 skill 값이 높은 상담원에게 우선적으로 배분합니다.");
		
	}
}
```

<br>

입력 문자에 따라 배분 정책 수행하기
```java
package scheduler;

import java.io.IOException;

public class SchedulerTest {

	public static void main(String[] args) throws IOException {

		System.out.println("전화 상담 할당 방식을 선택 하세요.");
		System.out.println("R : 한명씩 차례로 할당 ");
		System.out.println("L : 쉬고 있거나 대기가 가장 적은 상담원에게 할당 ");
		System.out.println("P : 우선순위가 높은 고객 먼저 할당 ");
		
        //입력 받은 값을 변수 ch에 저장
		int ch = System.in.read();
        //Scheduler 자료형 변수 선언
		Scheduler scheduler = null;
		
        //입력한 값에 따라 해당되는 인스턴스가 scheduler에 대입됨  
		if(ch == 'R' || ch == 'r'){
			scheduler = new RoundRobin();
		}
		else if(ch == 'L' || ch == 'l'){
			scheduler = new LeastJob();
		}
		else if(ch == 'P'|| ch == 'p'){
			scheduler = new PriorityAllocation();
		}
		else{
			System.out.println("지원되지 않는 기능입니다.");
			return;
		}
		
        //인터페이스를 활용해 다형성 구현ㅋ
		scheduler.getNextCall();
		scheduler.sendCallToAgent();
	}
}
```

<br>

## 2. 인터페이스의 요소

### 1) 인터페이스 상수
인터페이스는 추상 메서드로 이루어지므로 인스턴스를 생성할 수 없으며 멤버 변수도 사용할 수 없다. 따라서 인터페이스에 선언한 변수는 컴파일 과정에서 상수로 변환된다.

<br>

### 2) 디폴트 메서드
인터페이스에는 메서드를 구현할 수 없으므로 추상 메서드를 선언하고 각 클래스마다 똑같이 그 기능을 반복하려면 번거롭다. 따라서, 인터페이스에서 기본으로 제공되는 메서드가 필요한데 이를 '디폴트 메서드'라고 한다. 디폴트 메서드는 클래스에서 따로 구현하지 않아도 된다. 선언 시 default 예약어를 사용한다.

<br>
 
### 3) 정적 메서드
정적 메서드는 static 예약어를 사용하여 선언하면 클래스 생성과 무관하게 사용할수 있다. 정적 메서드를 사용할 때는 인터페이스 이름으로 직접 참조하여 사용한다.

<br>

### 4) private 메서드
private 메서드는 인터페이스를 구현한 클래스에서 사용하거나 재정의할 수 없다, 따라서 기존에 구현된 코드를 변경하지 않고 인터페이스를 구현한 클래스에서 공통으로 사용하는 경우에 pirvate 메서드로 구현하면 코드의 재사용성을 높일 수 있다.   
pirvate 메서드는 defautl 메서드에서, private static 메서드는 static 메서드에서 호출해 사용한다.

<br>

```java
package interfaceex;

public interface Calc {
	
	//상수
	double PI = 3.14;
	int ERROR = -999999999;
	
	int add(int num1, int num2);
	int substract(int num1, int num2);
	int times(int num1, int num2);
	int divide(int num1, int num2);
	
	//디폴트 메서드
	default void description(){
		System.out.println("정수 계산기를 구현합니다");
		myMethod();  //private 메서드 호출
	}
	
	//정적 메서드
	static int total(int[] arr){
		
		int total = 0;
		
		for(int i: arr){
			total += i;
		}
		myStaticMethod(); //private static 메서드 호출
		return total;
	}
	
	private void myMethod() {
		System.out.println("private 메서드 입니다.");
	}
	
	private static void myStaticMethod() {
		System.out.println("private static 메서드 입니다.");
	}
}
```

<br>

```java
package interfaceex;

public class CalculatorTest {

	public static void main(String[] args) {

		int num1 = 10;
		int num2 = 5;
		
		CompleteCalc calc = new CompleteCalc();
		System.out.println(calc.add(num1, num2));
		System.out.println(calc.substract(num1, num2));
		System.out.println(calc.times(num1, num2));
		System.out.println(calc.divide(num1, num2));
		calc.showInfo();
		
		//디폴트 메서드 사용하기
		calc.description();

        //정적 메서드 사용하기
		int[] arr={1,2,3,4,5};
		system.out.pirintln(Calc.total(arr));
		
	}}
```

#### 실행결과
15 
5        
50                               
2                      
Calc 인터페이스를 구현하였습니다                 
정수 계산기를 구현합니다               
private 메서드 입니다.              
private static 메서드 입니다.              
15                
     
<br>

## 4. 인터페이스 활용하기

### 1) 한 클래스가 여러 인터페이스를 구현하는 경우

Buy
```java
package interfaceex;

public interface Buy {
	void buy();

    //디폴트 메서드
default void order(){
	system.out.println("구매주문");
   }  
}
```

<br>

Sell
```java
package interfaceex;

public interface Sell {
	void sell();

//디폴트 메서드
default void order(){
	System.out.println("판매주문");
ㄴ}
}
```

<br>

Buy, Sell 인터페이스를 구현한 Customer 클래스
```java
package interfaceex;

public class Customer implements Buy, Sell{
	//Buy, Sell 인터페이스 모두 구현

	@Override
	public void buy() {
		System.out.println("구매하기");
	}

	@Override
	public void sell() {
		System.out.println("판매하기");

    //디폴트 메서드가 중복되는 경우 오류가 나기 때문에 재정의를 해야한다.
	@Override
	public void order() {
		System.out.println("고객 판매 주문");
	}
	}
}
```

<br>

```java
package interfaceex;

public class CustomerTest {

	public static void main(String[] args) {

		Customer customer = new Customer();
	    
		//Buy 인터페이스형으로 형변환
		Buy buyer = customer;
		buyer.buy();    //Buy 인터페이스 메서드만 호출 가능
		buyer.order();  //재정의된 메서드 호출
		
		//Sell 인터페이스형으로 형변환
		Sell seller = customer;
		seller.sell();   //Sell 인터페이스 메서드만 호출 가능
		seller.order();  //재정의된 메서드 호출
		
		if( seller instanceof Customer){  //하위 클래스형인 Customer로 다시 형변환
			Customer customer2 = (Customer)seller;
			customer2.buy();  //Customer형이므로 buy, sell 둘다 호출 가능
			customer2.sell();
		}
		customer.order();
	}
}
```

#### 출력결과
구매하기     
고객 판매 주문                  
판매하기              
고객 판매 주문         
구매하기                        
판매하기            
고객 판매 주문              

<br>

### 2) 인터페이스 상속하기


```java
package interfaceex;

public interface X{
	void x();
}
```

<br>

```java
package interfaceex;

public interface Y{
	void y();
}
```

<br>

X, Y 인스턴스를 상속받은 MyInterface
```java
public interface MyInterface extends X,Y{
	void myMethod();
}
```


<br>

MyInterface를 상속받은 MyClass
```java
package interfaceex;

public class MyClass implements MyInterface{
	//MyInterface는 X,Y 인터페이스를 상속받았으므로 x(), y() 클래스도 구현해야함

	@Override
	public void x() {
		System.out.println("x()");
	}

	@Override
	public void y() {
		System.out.println("y()");
	}

	@Override
	public void myMethod() {
		System.out.println("myMethod()");		
	}
}
```

<br>

```java
package interfaceex;

public class MyClassTest {

	public static void main(String[] args) {

		MyClass mClass = new MyClass();
		X xClass = mClass;
		xClass.x();  //X 인터페이스 메서드만 호출 가능
		
		Y yClass = mClass;
		yClass.y();  //Y 인터페이스 메서드만 호출 가능
		
		MyInterface iClass = mClass;
		iClass.myMethod();  //모두 호출 가능
		iClass.x();
		iClass.y();
	}
}
```

### 3) 인터페이스 구현과 클래스 상속 함께 쓰기

<br>

Shelf
```java
package bookshelf;

import java.util.ArrayList;

public class Shelf {
	
	//자료를 순서대로 저장할 ArrayList 선언
	protected ArrayList<String> shelf;

	//디폴트 생성자로 Shelf 클래스를 생성하면 ArrayList도 생성됨
	public Shelf(){
		shelf=new ArrayList<String>();
	}
	
	public ArrayList<String> getShelf(){
		return shelf;
	}

	public int getCount() {
		return shelf.size();
	}
}

```

<br>

Queue
```java
package bookshelf;

public interface Queue {
	void enQueue(String title);  //배열의 맨 마지막에 추가
	String deQueue();  //배열의 맨 처음 항목 반환
	int getSize();  //현재 Queue에 있는 개수 반환
}

```

<br>

Shelf 클래스 상속받고, Queue 인터페이스 구현한 BookShelf
Shelf 클래스가 가지고 있는 ArrayList 배열을 사용하여 Queue 인터페이스에서 선언한 메서드를 모두 구현
```java
package bookshelf;

public class Bookshelf extends Shelf implements Queue {

	// 배열에 요소 추가
	@Override
	public void enQueue(String title) {
		shelf.add(title);
	}
	
	//맨 처음 요소를 배열에서 삭제하고 반환
	@Override
	public String deQueue() {
		return shelf.remove(0);
	}

	//배열 요소 개수 반환
	@Override
	public int getSize() {
		return getCount();
	}

}
```

<br>

BookShelfTest
```java

package bookshelf;

public class BookShelfTest {

	public static void main(String[] args) {

		Queue shelfQueue = new BookShelf();
		
		//순서대로 요소를 추가
		shelfQueue.enQueue("태백 산맥 1");
		shelfQueue.enQueue("태백 산맥 2");
		shelfQueue.enQueue("태백 산맥 3");
		
		//입력 순서대로 요소를 꺼내서 출력
		System.out.println(shelfQueue.deQueue());
		System.out.println(shelfQueue.deQueue());
		System.out.println(shelfQueue.deQueue());
		
	}
}
```