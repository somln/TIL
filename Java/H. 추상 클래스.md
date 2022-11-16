# 추상 클래스

## 1. 추상 클래스

### 1) 추상 클래스란?
하나 이상의 추상 메서드(구현 코드가 없는 메서드)를 포함하는 클래스로, 실체클래스의 공통적인 부분(변수,메서드)를 추출해서 선언한 클래스이다. 하위 클래스에서 내용을 각각 다르게 구현해야 한다면, 구현 내용을 추상 메서드로 남겨두고 하위 클래스에 구현을 위임한다. 따라서, 상속을 위한 메서드라고 할 수 있다. 실체성이 없고 구체적이지 않기 때문에 인스턴스를 생성할 수 없다.

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

<br>

## 2. 템플릿 메서드
### 1)  템플릿 메서드란?
* 메서드 실행 순서와 시나리오를 정의
* 템플릿 메서드가 호출하는 메서드가 추상 메서드라면 하위 클래스에 따라 구현 내용이 바뀔 수는 있다.
* 하지만, 실행 순서나 시나리오는 바뀔 수 없기 때문에 final 예약어를 사용해서 재정의 할 수 없게 한다.

<br>

### 2) 템플릿 메서드 구현
Car
```java
package template;

public abstract class Car {
	
	//추상 메서드
	public abstract void drive();
	public abstract void stop();
	
	//구현코드는 없지만 구현은 한 상태
	//필요에 따라 하위 클래스에서 구현
	public void washCar() {};
	
	public void startCar() {
		System.out.println("시동을 켭니다.");
	}
	
	public void turnOff() {
		System.out.println("시동을 끕니다.");
	}
	
	//==템플릿 메서드==
	final public void run() {
		startCar();
		drive();
		stop();
		washCar();
		turnOff();
	}
}

```

<br>

AICar
```java
package template;

public class AICar extends Car {

	@Override
	public void drive() {
		System.out.println("자유 주행합니다.");
		System.out.println("자동차가 알아서 방향을 전환합니다.");

	}

	@Override
	public void stop() {
		System.out.println("스스로 멈춥니다.");

	}
	
	public void washCar() {
		System.out.println("자동으로 세차가 됩니다.");
	}
}

```

<br>

ManualCar
```java
package template;

public class ManualCar extends Car {

	@Override
	public void drive() {
		System.out.println("사람이 운전합니다.");
		System.out.println("사람이 핸들을 조작합니다.");
	}

	@Override
	public void stop() {
		System.out.println("브레이크로 정지합니다.");

	}
}
```

<br>

CarTest
```java
package template;

public class CatTest {

	public static void main(String[] args) {
		
	System.out.println("=== 자율 주행하는 자동차 ===");
	Car myCar = new AICar(); //Car형으로 형변환된 AICar 인스턴스 생성
	myCar.run();
	
	System.out.println("=== 사람이 운전하는 자동차 ===");
	Car hisCar = new ManualCar();  //Car형으로 형변환된 ManualCar 인스턴스 생성
	hisCar.run();
	}
}
```
#### 출력 결과
=== 자율 주행하는 자동차 === 
시동을 켭니다.                                      
자유 주행합니다.         
자동차가 알아서 방향을 전환합니다.                  
스스로 멈춥니다.     
자동으로 세차가 됩니다.                      
시동을 끕니다.                  
=== 사람이 운전하는 자동차 ===              
시동을 켭니다.                
사람이 운전합니다.              
사람이 핸들을 조작합니다.             
브레이크로 정지합니다.            
시동을 끕니다.          

템플릿 메서드에서 구현해놓은 순서대로 메서드가 실행된다. 

startCar(); -> 공통으로 출력                    
drive(); -> 재정의한 메서드 출력                               
stop(); -> 재정의한 메서드 출력                
washCar(); -> AICar에서만 재정의 하였기 때문에 AICar에서만 출력    
turnOff(); -> 공통으로 출력        

<br>

## 3. 템플릿 메서드 응용하기
#### 예제 시나리오
Player가 있고, 이 Player가 게임을 한다. 게임에서 Player가 가지는 레벨에 따라 할 수 있는 세가지 기능이 있다.           
* 초보자 레벨: 천천히 run
* 중급자 레벨: 빠르게 run, jump
* 고급자 레벨: 엄청 빠르게 run, jump, turn     
모든 레벨에서 Player가 사용할 수 있는 필살기인 go 메서드를 제공한다.
<img src="https://velog.velcdn.com/images%2Ffoeverna%2Fpost%2Fb8b7ae4c-3507-4ed9-8eca-509ee2200f47%2Fskdjfsf.png"></img>

PlayerLevel
```java
package gamelevel;

public abstract class PlayerLevel {
	
	//추상 메서드 -> 각 기능은 해당 레벨 클래스에서 구현
	public abstract void run();
	public abstract void jump();
	public abstract void turn();
	public abstract void showLevelMessage();
	
	//***템플릿 메서드***
	final public void go(int count) {
		run();
		for(int i=0; i<count; i++) {
			jump();
		}
		turn();
	}
}

```

<br>

BeginnerLevel
```java
package gamelevel;

public class BeginnerLevel extends PlayerLevel {

	@Override
	public void run() {
		System.out.println("천천히 달립니다.");
	}

	@Override
	public void jump() {
		System.out.println("jump X");
	}

	@Override
	public void turn() {
		System.out.println("Turn X");
	}

	@Override
	public void showLevelMessage() {
		System.out.println("***** 초보자 레벨입니다. *****");
	}

}

```

<br>

AdvancedLevel
```java
package gamelevel;

public class AdvancedLevel extends PlayerLevel {

	@Override
	public void run() {
		System.out.println("빨리 달립니다.");
	}

	@Override
	public void jump() {
		System.out.println("높이 Jump 합니다.");
	}

	@Override
	public void turn() {
		System.out.println("Turn X");
	}

	@Override
	public void showLevelMessage() {
		System.out.println("***** 중급자 레벨입니다. *****");
	}

}

```

<br>

SuperLevel
```java
package gamelevel;

public class SuperLevel extends PlayerLevel {

	@Override
	public void run() {
		System.out.println("엄청 빨리 달립니다.");
	}

	@Override
	public void jump() {
		System.out.println("아주 높이 Jump 합니다.");
	}

	@Override
	public void turn() {
		System.out.println("한 바퀴 돕니다.");
	}

	@Override
	public void showLevelMessage() {
		System.out.println("***** 고급자 레벨입니다. *****");
	}
}

```

<br>

Player
```java
package gamelevel;

public class Player {

	private PlayerLevel level; //PlayerLevel 자료형 level 참조변수 생성
	
	public Player() { //player 생성자
		level = new BeginnerLevel();  //BeginnerLevel 인스턴스를 생성하여 level 변수에 대입
		level.showLevelMessage(); //BeginnerLevel의 메세지 출력
	}
	
	public PlayerLevel getLevel() {
		return level;
	}
	
	public void upgradeLevel(PlayerLevel level) {  //상위 클래스인 PlayerLevel 자료형을 매개변수로
		this.level=level;  //인자로 들어온 playerLevel형 인스턴스를 level에 대입
		level.showLevelMessage(); //해당 레벨의 메세지 출력
	}
	
	public void play(int count) { //점프 횟수를 매개변수로 받으면
		level.go(count); //playerLevel의 템플릿 메서드 실행
	}
	
}
```

<br>

MainBoard
```java
package gamelevel;

public class MainBoard {
	
	public static void main(String[] args) {
		
		Player player1 = new Player(); 
		//player 인스턴스를 생성하여 player1에 대입
		//player1이 생성되면서 player1의 level 변수에 BeginnerLevel 인스턴스 대입
		//playerLevel의 showLevelMessage는 추상 메서드이기 때문에, BeginnerLevel.showLevelMessage 실행 

		player1.play(1); 
		//level.go(1)에 의해서 템플릿 메서드 실행
		//run(), jump(), turn() 모두 추상메서드로 BeginnerLevel의 메서드가 실행됨
		
		AdvancedLevel aLevel = new AdvancedLevel();
		// AdvancedLevel의 인스턴스를 생성하여 aLevel 변수에 대입
		player1.upgradeLevel(aLevel);
		//aLevel이 upgradeLevel 메서드의 인자로 들어가면서 AdvancedLevel->PlayerLevel 형변환
		//player1의 level에는 aLevel에 저장된 AdvancedLevel 인스턴스의 주소가 대입됨 
		player1.play(2);
		//level.go(2)에 의해서 템플릿 메서드 실행
		//run(), jump(), turn() 모두 추상메서드로 AdvancedLevel의 메서드가 실행됨
	
		SuperLevel sLevel = new SuperLevel();
		// SuperLevel의 인스턴스를 생성하여 sLevel 변수에 대입
		player1.upgradeLevel(sLevel);
		//sLevel이 upgradeLevel 메서드의 인자로 들어가면서 SuperLevel->PlayerLevel 형변환
		//player1의 level에는 sLevel에 저장된 SuperLevel 인스턴스의 주소가 대입됨 
		player1.play(3);
		//level.go(3)에 의해서 템플릿 메서드 실행
		//run(), jump(), turn() 모두 추상메서드로 SuperLevel의 메서드가 실행됨	
	}
}
```

<br>

## 4. final 예약어
* 변수: final 변수는 상수를 의미한다.
* 메서드: final 메서드는 하위 클래스에서 재정의할 수 없다.
* 클래스: final 클래스는 상속할 수 없다.

#### 여러 자바 파일에서 공유하는 상수 값 정의하기

```java
package finalex;

public class Define {

	public static final int MIN = 1;
	public static final int MAX = 99999;

	public static final int ENG = 1001;
	public static final int MATH = 2001;
	
	public static final double PI = 3.14;
	public static final String GOOD_MORNING = "Good Morning!";
}
```
* Define.java 파일을 하나 만들고 프로그램에서 사용할 상수 값들을 선언
* 모든 상수를 static으로 선언했기 때무에 인스턴스를 생성하는 것과 관계업싱 클래스 이름으로 참조

<br>

상수를 사용하는 예제 코드
```java
package finalex;

public class UsingDefine {

	public static void main(String[] args) {

		System.out.println(Define.GOOD_MORNING);   //static 으로 선언되었으므로 클래스 이름으로 참조 합니다.
		System.out.println("최솟값은 " +  Define.MIN + "입니다.");
		System.out.println("최댓값은 " +  Define.MAX + "입니다.");
		System.out.println("수학 과목 코드 값은 " + Define.MATH + "입니다.");
		System.out.println("영어 과목 코드 값은 " + Define.ENG + "입니다.");
		
	}

}
```