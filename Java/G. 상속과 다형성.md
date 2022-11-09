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
* 고객의 정보를 활용하여 고객 맞춤 서비를 구현      
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
	public VIPCustomer(int customerID, String customerName)
	{
		super(customerID, customerName); //상위 클래스 생성자를 호출할 때 매개변수 전달
		customerGrade = "VIP";  
		bonusRatio = 0.05;  
		saleRatio = 0.1;  
	}
	
```

<br>

CustomerTest1
```java
package inheritance;

public class CustomerTest1 {
	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10100, "Lee");
		VIPCustomer customerKim = new VIPCustomer(10101, "Kim");
		
		System.out.println(customerLee.showCustomerInfo());
		System.out.println(customerKim.showCustomerInfo());
	}
}
```

<br>

### 3) 상위 클래스로 묵시적 클래스 형 변환
VIPCustomer는 VIPCustomer형이면서 동시에 Customer 형이기도 하다. 즉, VIPCustomer 클래스로 인스턴스를 생성할 때 이 인스턴스 자료형을 Customer형으로 클래스 형 변환하여 선언할 수 있다.-->upcasting

```java
Customer customerPark = new VIPCustomer();
```
--> VIPCustomer() 생성자의 호출로 인스턴스는 모두 생성되었지만, 타입이 Customer 이므로 접근할 수 있는 변수나 메서드는 Customer의 변수와 메서드이다.