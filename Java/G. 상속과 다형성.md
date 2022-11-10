# 상속과 다형성

## 1. 상속이란?
### 1) 상속 개념
클래스 생성시 부모 클래스의 속성을 자식 클래스가 물려 받는 것  
부모 클래스: 더 일반적인 개념       
자식 클래스: 더 구체적인 개념

<br>

### 2) 클래스 상속 문법
```java
class Mammal{
    ...
}
```
  ↑
```java
class Human extends Mammal{
    ...
}
```

<br>

### 3) 상속을 활용한 고객관리 프로그램
* 고객의 정보를 활용하여 고객 맞춤 서비스를 구현      
* 고객의 등급에 따라 차변화 된 할인율과 포인트를 지급
* 등급에 따른 클래스를 따로 구현하는 것이 아닌 일반적인 클래스를 먼저 구현하고 그 보다 기능이 많은 클래스는 상속을 활용하여 구현함

<br>

#### ※ 상위 클래스 변수를 사용하기 위한 protected 예약어    
* 상위 클래스에서 작성한 변수나 메서드 중 외부 클래스에서 사용할 수 없지만 하위 클래스에서는 사용할 수 있도록 지정하는 예약어 
* 같은 패키지가 아니라도 상속 관계이면 외부에서 사용할 수 있다.

<br>

☞ 예약어 정리
* private: 해당 클래스에서만 접근할 수 있다. 
* default: 같은 패키지 내에서만 접근할 수 있다.
* protected: 다른 패키지여도 상속 관계이면 접근할 수 있다.
* public: 제한 없이 접근할 수 있다.

<br>

Customer
* 고객등급: SILVER      
* 보너스 포인트: 1%
```java
package inheritance;

public class Customer {
	
	protected int customerID; //고객 아이디
	protected String customerName; //고객 이름
	protected String customerGrade; //고객 등급
	int bonusPoint; //구매시 적립되는 포인트
	double bonusRatio; //포인트 적립 비율
	
	//고객이 처음 생성됬을 때 디폴트값
	public Customer()
	{
		customerGrade = "SILVER";  //고객 등급: silver
		bonusRatio = 0.01;  //적립 비율 :0.01
	}
	
	//구매 시 적립되는 포인트 계산
	public int calcPrice(int price){
		bonusPoint += price * bonusRatio;
		return price;
	}
	
	//고객 정보 출력
	public String showCustomerInfo(){
		return customerName + " 님의 등급은 " + customerGrade + "이며, 보너스 포인트는 " + bonusPoint + "입니다.";  
	}

	
	public int getCustomerID() {
		return customerID;
	}

	public void setCustomerID(int customerID) {
		this.customerID = customerID;
	}

	public String getCustomerName() {
		return customerName;
	}

	public void setCustomerName(String customerName) {
		this.customerName = customerName;
	}

	public String getCustomerGrade() {
		return customerGrade;
	}

	public void setCustomerGrade(String customerGrade) {
		this.customerGrade = customerGrade;
	}

}

```

<br>

VIPCustomer
* 고객 등급:
* 제품 구매 할인율:
* 보너스 포인트: 5%
* 담당 전문 상담원 배정

```java
package inheritance;

public class VIPCustomer extends Customer{

	private int agentID;  //상담원 아이디
	double saleRatio; //할인율
	
	public VIPCustomer()
	{
		customerGrade = "VIP";  // 고객 등급: VIP 
		bonusRatio = 0.05;  // 적립 비율: 0.05
		saleRatio = 0.1;  //할인율: 0.1
	}
	
	//담당자는 바꿀 수 없기 때문에 get 메서드만 지원
	public int getAgentID() {
		return agentID;
	}
}
```

<br>

CustomerTest1
```java
package inheritance;

public class CustomerTest1 {
	public static void main(String[] args) {
		
		Customer customerLee = new Customer();
		customerLee.setCustomerID(10100);
		customerLee.setCustomerName("Lee");
		
		VIPCustomer customerKim = new VIPCustomer();
		customerKim.setCustomerID(10101);
		customerKim.setCustomerName("Kim");
		
		System.out.println(customerLee.showCustomerInfo());
		System.out.println(customerKim.showCustomerInfo());
	}
} 
```

<br>

## 2. 상속에서 클래스 생성과 형 변환

### 1) 하위 클래스가 생성되는 과정
* 하위 클래스가 생성될 때 상위 클래스가 먼저 만들어진다. 
* super() 예약어는 하위 클래스에서 상위 클래스로 접근할 때 사용한다. 
* super()을 입력하지 않아도 자동으로 하위 클래스 생성자에서 호출된다.
* super()를 호출하면 상위 클래스의 디폴트 생성자가 호출된다.

<br>

### 2) super 예약어로 매개변수가 있는 생성자 호출하기
Customer 클래스를 생성할 때 고객 ID와 이름을 매개변수로 받아서 생성하고자 한다.

Customer
```java
public Customer(int customerID, String customerName)
	{
		this.customerID=customerID;
		this.customerName=customerName;
		customerGrade = "SILVER"; 
		bonusRatio = 0.01; 
	}
```

<br>

VIPCustomer
```java
	public VIPCustomer(int customerID, String customerName, int agentID)
	{
		super(customerID, customerName); //상위 클래스 생성자를 호출할 때 매개변수 전달
		customerGrade = "VIP";  
		bonusRatio = 0.05;  
		saleRatio = 0.1;  
		this.agentID=agentID;
	}
	
```

<br>

CustomerTest1
```java
package inheritance;

public class CustomerTest1 {
	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10100, "Lee");
		VIPCustomer customerKim = new VIPCustomer(10101, "Kim", 10);
		
		System.out.println(customerLee.showCustomerInfo());
		System.out.println(customerKim.showCustomerInfo());
	}
}
```

<br>

### 3) 상위 클래스로 묵시적 클래스 형 변환
VIPCustomer는 VIPCustomer형이면서 동시에 Customer 형이기도 하다. 즉, VIPCustomer 클래스로 인스턴스를 생성할 때 이 인스턴스 자료형을 Customer형으로 클래스 형 변환하여 선언할 수 있다.-->upcasting

```java
Customer customerWho = new VIPCustomer();
```
--> VIPCustomer() 생성자의 호출로 인스턴스는 모두 생성되었지만, 타입이 Customer 이므로 접근할 수 있는 변수나 메서드는 Customer의 변수와 메서드이다.   
-->> 따라서 다음과 같은 코드는 실행되지 않는다.
```java
Customer customerWho = new VIPCustomer(10102, "Who", 11);
System.out.println(customerWho.getAgentID());
```

<br>

## 3. 메서드 오버라이딩
### 1) 상위 클래스 메서드 재정의하기

* 메서드 오버라이딩이란 상위 클래스에서 정의한 메서드가 하위 클래스에서 구현할 내용과 맞지 않을 경우 하위 클래스에서 해당 메서드를 재정의하는 것    
* 오버리아딩을 하려면 반환형, 메서드 이름, 매개 변수 개수, 매개 변수 자료형이 반드시 같아야 한다.

* VIP 고객의 경우 정가에서 10% 할인을 받을 수 있기 때문에 상의 클래스의 calcPrice() 메서드를 그대로 쓸 수 없다. 따라서 이 메서드를 재정의하였다.

VIPCustomer
```java
package inheritance;

public class VIPCustomer extends Customer{

	private int agentID;  
	double saleRatio; 
	
	public VIPCustomer(int customerID, String customerName, int agentID)
	{
		super(customerID, customerName); 
		customerGrade = "VIP";  
		bonusRatio = 0.05; 
		saleRatio = 0.1; 
		this.agentID=agentID;
	}
	
	public int calcPrice(int price){
		bonusPoint += price * bonusRatio;
		return price - (int)(price*saleRatio);
	}
	
	//담당자는 바꿀 수 없기 때문에 get 메서드만 지원
	public int getAgentID() {
		return agentID;
	}
}
```

<br>

CustomerTest1

```java
package inheritance;

public class CustomerTest1 {
	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10100, "Lee");
		VIPCustomer customerKim = new VIPCustomer(10101, "Kim",10);

		System.out.println("지불 금액은 "+customerLee.calcPrice(10000)+"원이고, " +customerLee.showCustomerInfo());
		//지불 금액은 10000원이고, Lee 님의 등급은 SILVER이며, 보너스 포인트는 100입니다.

		System.out.println("지불 금액은 "+customerKim.calcPrice(10000)+"원이고, "+customerKim.showCustomerInfo());
		//지불 금액은 9000원이고, Kim 님의 등급은 VIP이며, 보너스 포인트는 500입니다.
	}
}
```
--> customerLee는 Customer Class의 calaPrice가, customerKimdms VIPCustomer Class의 calaPrice가 호출되었다.

<br>

### 2) 가상메서드
묵시적 형 변환에 의해 VIPCustomer가 Customer 형으로 변환되었을 때 calaPrice()는 어떤 클래스의 메서드를 호출하는 지 확인하면,

```java
Customer customerWho = new VIPCustomer(10102, "Who", 11);
System.out.println("지불 금액은 "+customerWho.calcPrice(10000)+"원이고, "+customerKim.showCustomerInfo());
//지불 금액은 9000원이고, Kim 님의 등급은 VIP이며, 보너스 포인트는 500입니다.
```
--> 출력 결과 VIPCustomer에서 재정의된 메서드가 호출되었다.     

-->> 상속에서 상위 클래스와 하위 클래스에 같은 이름의 메서드가 존재할 때 호출되는 메서드는 선언한 클래스형이 아닌 인스턴스의 메서드가 호출된다. 이렇게 인스턴스 메서드가 호출되는 기술을 <u>'가상 메서드'</u>라고 한다.

<br>

## 4. 다형성
### 1) 다형성이란?
다형성이란 하나의 코드가 여러 자료형으로 구현되어 실행되는 것을 말한다. 쉽게 말해 같은 코드에서 여러 실행 결과가 나오는 것이다.
 
AnimalTest1
```java

package inheritance;

class Animal{
	public void move() {
		System.out.println("동물이 움직입니다.");
	}
}

class Human extends Animal{
	public void move() {
		System.out.println("사람이 두 발로 걷습니다.");
	}
}

class Tiger extends Animal{
	public void move() {
		System.out.println("호랑이가 네 발로 뜁니다.");
	}
}

class Eagle extends Animal{
	public void move() {
		System.out.println("독수리가 하늘을 납니다.");
	}
}

public class AnimalTest1 {
	public static void main(String[] args) {
		AnimalTest1 aTest = new  AnimalTest1();
		aTest.moveAnimal(new Human());
		aTest.moveAnimal(new Tiger());
		aTest.moveAnimal(new Eagle());
		
		Animal animal = new Human();
	}
	
	public void moveAnimal(Animal animal) {
		animal.move();
	}
}

```
1. 상위 클래스 Animal 생성, move 메서드 생성
2. 하위 클래스 Human, Tiger, Eagle 생성, move 메서드 오버라이딩
3. 메인함수를 포함하는 클래스 AnimalTest1 생성, moveAnimal 메서드 생성, moveAnimal 메서드를 사용하기 위한 AnimalTest1 인스턴스 생성
4. moveAnimal()메서드에 Human 인스턴스를 생성하여 인자로 전달
5. moveAnimal()메서드는 Animal형을 매개변수로 가지고 있기 때문에 어떤 인자가 넘어와도 모두 Animal 형으로 변환    
   따라서 Human 인스턴스가 전달되었다면, 다음과 같이 형 변환됨. Animal animal = new Human(); 
6. Animal형으로 변환된 Human 인스턴스는 animal.move()메서드를 호출
7. 가상 메서드 원리에 따라 animal.move() 메서드가 호출하는 메서드는 Animal의 move가 아닌 Human 인스턴스의 move 메서드가 실행됨
8. 나머지 코드도 같은 과정을 거치면, animal.move() 코드는 변함이 없지만 어떤 매개변수가 넘어왔느냐에 따라 출력문이 달라지는 것을 <u>'다형성'</u>이라고 함

#### 위 과정을 짧게 축약하면,   
1. 하위 클래스에서 상위 클래스를 상속받아 <u>메서드 오버라이딩</u>
2. 메인 함수에서 하위 클래스를 상위 클래스로 <u>묵시적 형 변환</u>
3. 하나의 코드로 상위 클래스의 메서드를 호출하면 <u>가상 메서드</u>의 원리에 따라 매개 변수로 넘어온 실제 인스턴스의 메서드 호출

#### 다형성의 장점
* 새로운 동물도 Animal 클래스를 상속받아 구현한 뒤, Animal 클래스로 형 변환을 하면 모든 클래스를 Animal 자료형 하나로 쉽게 관리할 수 있다.
* 상속받은 모든 클래스를 하나의 상위 클래스로 처리할 수 있고 다형성에 의해 각 클래스의 여러가지 구현을 쉽게 실행할 수 있으므로 프로그램을 쉽게 확장할 수 있다.

