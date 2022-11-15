# 추상 클래스

## 1. 추상 클래스

### 1) 추상 클래스란?
하나 이상의 추상 메서드(구현 코드가 없는 메서드)를 포함하는 클래스로, 실체클래스의 공통적인 부분(변수,메서드)를 추출해서 선언한 클래스이다. 하위 클래스에서 내용을 각각 다르게 구현해야 한다면, 구현 내용을 추상 메서드로 남겨두고 하위 클래스에 구현을 위임한다. 따라서, 상속을 위한 메서드라고 할 수 있다. 실체성이 없고 구체적이지 않기 때문에 인스턴스를 생설할 수 없다.

<br>

### 2) 추상 클래스 구현하기
Computer -> 추상 클래스
```java
package abstractEx;

public abstract class Computer { //abstract 예약어를 추가해 추상 클래스 선언
	
	public abstract void display(); //추상 메서드1 
	public abstract void typing(); //추상 메서드2
	
	public void turnOn() {  //구현 메서드1
		System.out.println("전원을 켭니다.");
	}
	
	public void turnOff() { //구현 메서드2
		System.out.println("전원을 끕니다.");
	}
}
```
<br>

DeskTop 
```java
package abstractEx;

public class DeskTop extends Computer{ //모든 메서드가 구현되었으므로 abstract 예약어X

	@Override
	public void display() {  //display 메서드 재정의
		System.out.println("DeskTop Display()");
	}

	@Override
	public void typing() {  //typing 메서드 재정의
		System.out.println("DeskTop Typing()");		
	}
}
```

<br>

NoteBook ->추상 클래스
```java
package abstractEx;

public abstract class  NoteBook extends Computer{ //display 메서드 하나만 구현했으므로 추상 클래스이다.

	@Override
	public void display() {
		System.out.println("NoteBook Display()");		
	}
}

```
<br>

MyNoteBook
```java
package abstractEx;

public class MyNoteBook extends NoteBook {   //모든 메서드가 구현되었으므로 abstract 예약어X

	@Override
	public void typing() {
		System.out.println("MyNoteBook Typing()");
	}
}


```
<br>

ComputerTest
```java
package abstractEx;

public class ComputerTest {

	public static void main(String[] args) {
		//Computer c1 = new Computer(); -> 인스턴스 생성 불가
		Computer c2 = new DeskTop();
		//Computer c3 = new NoteBook(); -> 인스턴스 생성 불가
		Computer c4 = new MyNoteBook();
		
		c2.display();
        //DeskTop Display()
		c2.typing();
        //DeskTop Typing()
		c4.display();
        //NoteBook Display()
		c4.typing();
        //MyNoteBook Typing()
    }
}

```