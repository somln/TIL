# 컬랙션 프레임워크

## 1. 제너릭
### 1) 제너릭이란?
어떤 값이 하나의 참조 자료형이 아닌 여러 참조 자료형을 사용할 수 있도록 프로그래밍하는 것을 '제너릭 프로그래밍'이라고 한다. 여러 참조 자료형이 쓰일 수 있는 곳에 특정한 자료형을 지정하지 않고, 클래스나 메서드를 정의한 후 사용하는 시점에 어떤 자료형을 사용할 것인지 지정하는 방식이다. 

<br>

### 2) 제너릭 클래스 정의하기
제네릭은 클래스와 메소드에서 사용할 수 있는데, 제네릭 타입을 선언한 클래스를 제네릭 클래스라 한다.

GenericPrinter
```java
package generics;

public class GenericPrinter<T> { //자료형 매개변수 T를 사용하는 클래스 GenericPrinter
	private T material;  // T 자료형 변수 material
	
	public void setMaterial(T material) {   //T 자료형 변수 material을 선언하는 메서드
		this.material = material;
	}
	
	public T getMaterial() {  // T 자료형 변수 material을 반환하는 제너릭 메서드
		return material;
	}
	
	public String toString(){  
		return material.toString();
	}
}
```
<br>

### 3) 제너릭 클래스 사용하기
 
 Powder
```java

package generics;

public class Powder{
		
	public void doPrinting() {
		System.out.println("Powder 재료로 출력합니다");
	}
	
	public String toString() {
		return "재료는 Powder 입니다";
	}
}
```

<br>

 Plastic
 ```java
package generics;

public class Plastic {
	
	public void doPrinting() {
		System.out.println("Plastic 재료로 출력합니다.");
	}
	
	public String toString(){
		return "재료는 Plastic입니다.";
	}
}
	
```

<br>

 GernericPrinterTest

 ```java
 package generics;

public class GenericPrinterTest {
	
	public static void main(String[] args) {
		
		GenericPrinter<Powder> powderPrinter = new GenericPrinter<Powder>();
		//GenericPrinter의 T에 Powder 클래스가 대입된 인스턴스를 생성하여 PowderPrinter에 대입
		 powderPrinter.setMaterial(new Powder());
		//Powder형 인스턴스를 생성하여 powderPrinter의 Powder형으로 선언된 material 변수에 대입
		System.out.println(powderPrinter); 
		// 재료는 Powder 입니다. 출력
		
		GenericPrinter<Plastic> plasticPrinter = new GenericPrinter<Plastic>();
		//GenericPrinter의 T에 Plastic 클래스가 대입된 인스턴스를 생성하여 PlasticPrinter에 대입
		plasticPrinter.setMaterial(new Plastic());
		//Plastic형 인스턴스를 생성하여 plasticPrinter의 Plastic형으로 선언된 material 변수에 대입
		System.out.println(plasticPrinter); 
		//재료는 Plastic입니다. 출력
	} 
}
```

<br>

### 4) 상속을 통해 자료형 제한하기
T 자료형에는 모든 자료형이 대입될 수 있다. T 자료형에 사용할 자료형을 제한하기 위해서는 제너릭 클래스를 선언할 때 extends 예약어로 제한을 둘 수 있다.
```<T extends Material>``` 와 같이 선언하면 Material Class를 상속받은 Class만 T에 대입될 수 있다. 또한, 이 경우 제너릭 클래스에서 상위 클래스 Material에 선언된 메서드를 모두 사용할 수 있다.

GenericPrinter
```java
package generics;

public class GenericPrinter<T extends Material> { //자료형 매개변수 T를 사용하는 클래스 GenericPrinter
	private T material;  // T 자료형 변수 material
	
	public void setMaterial(T material) {  
		this.material = material;
	}
	
	public T getMaterial() {  // T 자료형 변수 material을 반환하는 제너릭 메서드
		return material;
	}
	
	public String toString(){
		return material.toString();
	}
	
	public void printing() {
		material.doPrinting();
	}

}
```

<br>

Powder, Plastic
```java
public class Powder extends Material{...
public class Plastic extends Material {...
```

<br>

GenericPrinterTest
```java
package generics;

public class GenericPrinterTest {
	
	public static void main(String[] args) {
		
		GenericPrinter<Powder> powderPrinter = new GenericPrinter<Powder>();
		powderPrinter.setMaterial(new Powder());
		powderPrinter.printing();  
		//power 재료로 출력합니다. 출력
		
		GenericPrinter<Plastic> plasticPrinter = new GenericPrinter<Plastic>();
		plasticPrinter.setMaterial(new Plastic());
		plasticPrinter.printing();
		//plastic 재료로 출력합니다. 출력
	} 
}
```

<br>

## 2. 컬랙션 프레임워크

### 1) 컬랙션 프레임 워크란?
자바에서는 프로그래밍에서 필요한 자료 구조를 미리 구현하여 java.util 패키지에서 제공하는데, 이를 컬랙션 프레임워크라고 한다. 전체 구조는 Collection 인터페이스와 Map 인터페이스를 기반으로 이루어져 있다.
<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2630264F548D957F09"></img>

<br>

### 2) Collenction 인터페이스
Collection 인터페이스는 하나의 자료를 모아서 관리하는데 필요한 기능을 제공한다.      
 하위 인터페이스
* List 인터페이스: 순차적인 자료를 관리하는데 사용하는 클래스가 구현됨
* Set 인터페이스: 순서가 정해지지 않으며 중복을 허락하지 않음

<br>

### 3) Map 인터페이스
Map 인터페이스는 하나가 아닌 쌍으로 되어있는 자료를 관리하는 메서드들이 선언되어 있다. key-value 쌍이라고 표현하는데 이 때 키 값은 중복될 수 없다.

<br>

## 3. List 인터페이스
### 1) ArrayList 클래스

Member 클래스
```java
package collection;

public class Member {
	
	private int memberID;
	private String memberName;
	
	public Member(int memberID, String memberName) {
		this.memberID=memberID;
		this.memberName=memberName;
	}
	
	
	public int getMemberID() {
		return memberID;
	}
	
	public void setMemberID(int memberID) {
		this.memberID = memberID;
	}

	public String getMemberName() {
		return memberName;
	}

	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}


	public String toString() {
		return memberName + "회원님의 아이디는 "+memberID+"입니다.";
		
	}
}
```

<br>

ArrayList 활용하기
```java
package collection.arraylist;

import java.util.ArrayList;  
import collection.Member;  //Member class는 다른 패키지에 존자해기 때문에 import를 해주어야한다

public class MemberArrayList {
	
	private ArrayList<Member> arrayList;  //ArrayList 자료형 선언
	
	public MemberArrayList(){
		arrayList=new ArrayList<Member>();  //MemberArrayList 클래스를 생설할 때 ArrayList 인스턴스 생성
	}
	
	public void addMember(Member member) {  //ArrayList에 회원을 추가하는 메서드
		arrayList.add(member);
	}
	
	public boolean removeMember(int memberID) {  //ArrayList에서 회원을 삭제하는 메서드
		for (int i=0; i<arrayList.size(); i++) { 
			Member member = arrayList.get(i);  //get()메서드로 회원을 순차적으로 가져옴
			int tempID = member.getMemberID();  //getMemberID() 메서드로 회원 아이디 가져옴
			
			if(tempID==memberID) {  //회원아이디가 매개변수와 일치하면
				arrayList.remove(i);  //해당 회원을 삭제
				return true;
			}
		}
		System.out.println(memberID+ "가 존재하지 않습니다.");  //return true가 실행되지 않고 내려왔다면 일치하는 아이디가 없는 것
		return false;
	}
	
	public void showAllMember() {
		for(Member member :arrayList){
		System.out.println(member);
	}
	System.out.println();
	
	}
	
}
```

<br>

ArrayList 테스트
```java
package collection.arraylist;

import collection.Member;

public class MemberArrayListTest {
	
	public static void main(String[] args) {
		MemberArrayList memberArrayList1 = new MemberArrayList();  
		//MemberArrayList 인스턴스가 생성되면서 ArrayList가 생성됨
		
		//Member 인스턴스 생성
		Member memberLee = new Member(1001, "이지원");  
		Member memberSon = new Member(1002, "손민국");  
		Member memberPark = new Member(1003, "박서훤");  
		Member memberHong = new Member(1004, "홍길동");  
		
		//Member 인스턴스를 ArrayList애 추가
		memberArrayList1.addMember(memberLee);
		memberArrayList1.addMember(memberSon);
		memberArrayList1.addMember(memberPark);
		memberArrayList1.addMember(memberHong);
		
		//전체 회원 출력
		memberArrayList1.showAllMember();
		
		//홍길동 회원 삭제
		memberArrayList1.removeMember(memberHong.getMemberID());
		//홍길동회원을 삭제한 후 다시 전체 회원 출력
		memberArrayList1.showAllMember();
		
	}
}
```

<br>

### 2) LinkedList 클래스
LinkedList 클래스에는 링크드 리스트 맨 앞 또는 맨 뒤에 요소를 추가-삭제하는 addFirst(), addLast(), removeFirst(), removeLast() 등의 메서드가 있다.
```java
package collection.linkedList;

import java.util.LinkedList;

public class LinkedListTest {
	public static void main(String[] args) {
		
		//LinkedList 자료형 인스턴스 선언
		LinkedList<String> myList = new LinkedList<String>();
		
		myList.add("A");
		myList.add("B");
		myList.add("C");
		
		System.out.println(myList);  //[A, B, C]
		
		myList.add(1,"D");  //1번째 위치에 D 추가
		System.out.println(myList);    //[A, D, B, C]
		
		myList.addFirst("0");  //맨 앞에 0추가
		System.out.println(myList);  //[0, A, D, B, C]
		
		System.out.println(myList.removeLast());  //C
		System.out.println(myList);   //[0, A, D, B]
		 
	}
}
```
<br>

### 3) ArrayList로 스택 구현하기
Stack 클래스와 Queue인터페이스는 제공되어 있지만, ArrayList나 LinkedList 클래스를 활용하여 구현하는 경우도 종종 있다.
```java
package collection.arraylist;

import java.util.ArrayList;

class MyStack {
	
	private ArrayList<String> stackArrayList = new ArrayList<>();
	
	//push 구현하기
	public void push(String data) {
		stackArrayList.add(data);
	}
	
	//pop 구현하기
	public String pop() {
		int len = stackArrayList.size(); //ArrayList에 저장된 유효한 자료의 개수 저장
		
		if (len==0) {
			System.out.println("스택이 비어있습니다.");
			return null;
		}
		return stackArrayList.remove(len-1); //맨 쥐에 있는 자료 반환하고 배열에서 제거
	}
	
	public String toString() {
		return stackArrayList.toString();
	}
	
}


public class StackTest {
	public static void main(String[] args) {
		
		MyStack stack = new MyStack();
		
		stack.push("A");
		stack.push("B");
		stack.push("C");
		
		
		System.out.println(stack); //[A, B, C]
		
		System.out.println(stack.pop());  //C
		System.out.println(stack.pop());  //B
		System.out.println(stack.pop());  //A
		
		System.out.println(stack);  //[]
		
		
	}
}
```

<br>

### 4) ArrayList로 큐 구현하기
```java
package collection.arraylist;

import java.util.ArrayList;

class MyQueue{
	
	private ArrayList<String> queueArrayList = new ArrayList<>();
	 
	public void enQueue(String data) {
		queueArrayList.add(data);
	}
	
	public String deQueue() {
		
		int len = queueArrayList.size();
		
		if (len==0) {
			System.out.println("스택이 비어있습니다.");
			return null;
		}
		return queueArrayList.remove(0); //맨 앞의 자료 반환하고 배열에서 제거
	}
	
	public String toString() {
		return queueArrayList.toString();
	}
}



public class QueueTest {

	public static void main(String[] args) {
		
		MyQueue queue = new MyQueue();
		
		queue.enQueue("A");
		queue.enQueue("B");
		queue.enQueue("C");
		
		System.out.println(queue);  //[A, B, C]
		System.out.println(queue.deQueue());  //A
		System.out.println(queue.deQueue());  //B
		System.out.println(queue.deQueue());  //C
		System.out.println(queue);  //[]
		
	}	
}
```
<br>

## 5) Collection 요소를 순회하는 Iterator
순서가 없는 Set 인터페이스를 구현한 경우에는 get(i) 메서드를 사용할 수 없는데, 이 때 Iterator를 사용한다. Iterator 는 collection 인터페이스를 구현한 객체이서 미리 정의되어 있는 iterator()메서드를 호출하여 참조한다. 예를 들어 Collection을 구현한 ArrayList에 iterator()메서드를 호출하면 Iterator 클래스가 반환되므로 다음 처럼 Iterator형 변수에 대입해 사용한다.
```java
Iterator ir = memberArrayList.iterator();
```
Iterator를 사용하여 모든 요소를 순회할 때 사용하는 메서드
* boolean hasNext(): 이후 요소가 더 있으면 true를 반환 
* E next(): 다음에 있는 요소를 반환

<br>

MemberArrayList 클래스의 removeMember()메서드 수정
```java
public boolean removeMember(int memberID) {  //ArrayList에서 회원을 삭제하는 메서드
		
		Iterator<Member> ir = arrayList.iterator();  //arrayList의 iterator메서드의 반환값을 사용하여 Iterator 형 변수 ir 선언
		while(ir.hasNext()) { //남아있는 요소가 있을 때 까지 반복
			Member member = ir.next();
			int tempID = member.getMemberID();
			if(tempID==memberID) {
				arrayList.remove(member);
				return true;
			}
		}
		
		System.out.println(memberID+ "가 존재하지 않습니다.");  //return true가 실행되지 않고 내려왔다면 일치하는 아이디가 없는 것
		return false;
	}
```