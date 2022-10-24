# 클래스와 객체

## 1. 객체 지향 프로그래밍

### 1) 절차 지향 프로그래밍, 객체 지향 프로그래밍
#### 절차 지향 프로그래밍          
: 순차적인 처리가 중요시 되며 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법  

ex) 아침에 일어난다 -> 씻는다 -> 밥을 먹는다 -> 버스를 탄다 -> 요금을 지불한다 -> 학교에 도착한다

####  객체 지향 프로그래밍                   
 : 프로그램 구현에 필요한 '객체'를 파악하고 각각의 객체들의 역할이 무엇인지를 정의하여 객체들 간의 '상호작용'을 통해 프로그램을 만드는 것 

 1. 객체 정의
 2. 객체의 기능 구현
 3. 객체 사이의 협력 구현

ex) 대상이 되는 객체: 학생, 밥, 버스, 학교         
* 밥을 먹는다 -> '학생'이라는 객체와 '밥'이라는 객체에 있어 학생이 밥을 먹는 협력으로 이루어진다.  (학생이 밥을 먹으면 밥의 양이 줄고 밥이 완전히 없어지면 학생은 밥을 다 먹은 것)           
* 버스를 탄다 -> '학생'이라는 객체와 '버스'라는 객체에 있어 학생이 버스에 타는 협력으로 이루어 진다. (학생이 버스를 타면 학생은 돈이 줄어들고 버스는 돈을 벌 수 있고 버스는 승객이 증가)

<br>

<img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F997F0E435C1E055B18"></img>

<br>

## 2. 클래스
### 1) 클래스
: 객체에 대한 속성과 기능을 코드로 구현한 것 

객체의 속성: 객체의 특성(속성)을 멤버 변수로 표현 ex) 학번, 이름, 학년, 사는 곳                        
객체의 기능: 객체가 하는 기능을 메서드로 구현 ex) 수강 신청, 수업 듣기, 시험 보기

* 클래스는 대부분 대문자로 시작
* 하나의 java 파일에는 하나의 클래스를 두는 것이 원칙,
* 여러개의 클래스가 같이 있는 경우 public 클래스는  단 하나
* public 클래스와 자바 파일의 이름은 동일해야함
* 자바의 모든 코드는 class 내부에 위치

```java
(접근 제어자) class 클래스 이름{
    멤버 변수;
    메서드;
}
```
```java
	public class Student{  //클래스 명
    // 멤버 변수
		int studentID;  //학번
		String studentName;  //이름
		int grade;  //학년
		String address;  //사는 곳

    //메서드
        public void showStudentInfor() {
	       System.out.println(studentName + ","+ address);
	    }
```
<br>

### 2) 패키지
: 클래스 파일의 묶음
* 프로젝트 전체 소스 코드를 구성하는 계층 구조
* 이름은 소문자로 시작
* 클래스 이름이 같아도 다른 패키지에 속해있으면 다른 클래스

<br>

## 3. 메서드

### 1) 함수
: 하나의 기능을 수행하는 일련의 코드 

```java
int add(int num1, int num2){
	int result;
	result=num1+num2
	return result;
}
```
* int: 함수 반환형
* add: 함수 이름
* num1, num2: 매개변수
* return: 함수 수행 결과를 반환하기 위한 예약어

<br>

### 2) 메서드
: 함수의 일종, 객체의 기능을 제공하기 위해 멤버 변수들을 이용해서 클래스 내부에 구현되는 함수

```java
	public class Student{  

		int studentID;  
		String studentName;  
		int grade;  
		String address;

		//메서드1
		public void showStudentInfo(){
		System.out.println(studentName + "," + address); 
	    }

		//메서드2
		public Stirng getStudentName(){
			return studentName;
		}
		//메서드3
		public void setStudentName(String name){
		    studentName = name;
		}
	}
```

<br>

## 4. 클래스 생성과 인스턴스

### 1) 클래스 생성 (인스턴스화)
* 클래스를 사용하기 위해서는 클래스를 생성해야 함
* new 예약어를 사용하여 클래스 생성
* 생성 방법: 클래스형 변수이름 = new 생성자;
 ```java
 Student studentAhn = new Student();
 ```
 * Student 클래스 자료형으로 studentAhn 변수를 선언하고 new Student();로 Student 클래스를 생성하여 studentAhn에 대입
 * 이때 studentAhn을 참조변수라고 하고, 이 변수는 생성된 인스턴스를 가리킨다.

<br>

 ### 2) 클래스 사용: main 함수를 생성하여 사용
 main 함수:
 JVM(자바 가상 머신)이 프로그램을 시작하기 위해 호출하는 함수
 

#### 1. class 내부에 main 함수를 포함하여 실행
class 내부에 생성되긴 하지만 class의 메서드는 아니다.
 ```java
package classpart;

public class Student {
	
	int studentID;
	String studentName;
	int grade;
	String address;
	
	public void showStudentInfo(){
		System.out.println(studentName + "," + address); 
	}
	
	public String getStudentName() {
		return studentName;
	}	
	
	public void setStudentName(String name){
		studentName = name;
	}
	
	public static void main(String[] args) {
		Student studentAhn = new Student();  //class 생성
		studentAhn.studentName = "안승연";
		studentAhn.studentID=100;
		studentAhn.adderss='서울시'
		
		System.out.println(studentAhn.studentName);
		System.out.println(studentAhn.getStudentName());
	}
 ```
<br>

 #### 2. main()함수를 포함한 실행 클래스 따로 만들기
 ```java
package classpart;

public class StudentTest {

	public static void main(String[] args) {

		Student studentAhn = new Student();
		studentAhn.studentName = "안승연"; 
		
		System.out.println(studentAhn.studentName);
		System.out.println(studentAhn.getStudentName());
	}
}
```
<br>

### 3) 인스턴스와 참조변수 
인스턴스 생성 과정
1. 참조 변수가 지역 변수로 선언되어 스택 메모리에 저장
2. 클래스 생성자를 호출하면 힙 메모리에 인스턴스가 생성됨
3. 생성된 클래스를 참조 변수에 대입하면, 인스턴스가 저장된 메모리를 참조변수가 가리킴 

* 스택 메모리: 함수가 호출되면 지역변수가 쌓이고 함수가 끝나면 그 스택이 자연스럽게 없어짐
* 힙 메모리: new라는 키워드에 의해서 생성되고, 가비지 컬랙터에 의해서 해제됨

 ```java
System.out.println(studentLee); 
//인스턴스가 저장된 메모리 주소가 출력됨
```
<br>

### ※용어 정리
* 객체: 객체 지향 프로그램의 대상, 생성된 인스턴스
* 클래스: 객체를 프로그래밍하기 위해 코드로 만든 상태
* 인스턴스: 클래스가 메모리에 생성된 상태
* 멤버 변수: 클래스의 속성, 특성
* 메서드: 멤버 변수를 이용하여 클래스에 기능을 구현
* 참조 변수: 메모리에 생성된 인스턴스를 가리키는 변수
* 참조 값: 생성된 인스턴스의 메모리 주소 값

<br>

## 5. 생성자
* Student studentAhn = new Student()애서 'Student()'
* 클래스를 생성할 때 멤버 변수나 상수를 초기화하는 역할을 한다.
* 객체가 생성될 때 수행되어야 하는 명령어 코드를 담고 있다.
* 생성자의 이름은 클래스의 이름과 같다.
* 메소드에 해당되지 않는다.
* 상속되지 않으며 리턴값은 없다.
* 하나의 클래스에는 반드시 하나의 생성자가 존재한다. (생성자가 없는 경우 디폴트 생성자 제공)

* 디폴트 생성자:
    * 생성자가 없는 클래스는 클래스 파일을 컴파일 할 때 자바 컴파일러에서 자동으로 생성자를 만들어주는데 이 생성자를 디폴트 생성자라고 한다.
	* 클래스에매개변수가 있는 생성자를 추가하면 디폴트 생성자는 제공되지 않는다.
	* 매개변수와 기능은 따로 존재하지 않는다. 

<br>

생성자 만들기
```java 
public class Student{
	int studentID;
	Stirng studentName;
	int grade;
	String address;

	public Student(int id, String name){
		studentID=id;
		studentName=name;
	}

	public static void main(Stirng[] args){
		Student studentLee=new Student();
		studentLee.studentName ="이순신";
		studentLee.studentID=100;
		studentLee.address="서울시";
	}
}
```

위와 같이 코드를 작성할 경우, 생성자를 직업 추가하여 디폴트 생성자가 만들어지지 않았기 때문에 에러가 발생한다.

<br>

해결 방법1: 매개변수가 있는 생성자로 호출한다. main함수에서 클래스를 생성할 때 생성자에게 매개변수를 입력해준다.       
```java 
public class Student{
	int studentID;
	Stirng studentName;
	int grade;
	String address;

	public Student(int id, String name){
		studentID=id;
		studentName=name;
	}

	public static void main(Stirng[] args){
		//이름을 매개변수로 받아 클래스를 생성한 경우
		Student studentLee=new Student(100,"이순신");
		studentLee.address="서울시";
	}
}
```
<br>

해결 방법 2: 디폴트 생성자를 직접 추가한다.         
-> "생성자 오버로드" : 같은 이름을 가진 생성자가 존재, 필요한 생성자를 골라서 사용 가능

```java 
public class Student{
	int studentID;
	Stirng studentName;
	int grade;
	String address;

	public Student(){};

	public Student(int id, String name){
		studentID=id;
		studentName=name;
	}

	public static void main(Stirng[] args){
		//디폴트 생성자로 클래스 생성
		Student studentLee=new Student();
		studentLee.studentName ="이순신";
		studentLee.studentID=100;
		studentLee.address="서울시";
	}
}
```
<br>

## 6. 참조 자료형 
: 클래스 자료형으로 선언하는 변수

하나의 클래스 안에 모든 정보를 다 저장할 필요는 없고, 변수가 늘어날 수록 코드가 길어지게 된다. 따라서 클래스 안에 클래스 자료형을 선언하여 더 편리하게 사용할 수 있다.

### 1) 클래스 자료형 생성하기

```java 
package reference;

public class Subject {

	String subjectName;
	int scorePoint;
}
```

```java 
package reference;

public class Student {

	int studentID;
	String studentName;
	Subject korean;
	Subject math;
	
	public Student(){
		korean = new Subject();
		math = new Subject();
	}
}
```
클래스 안에서 다른 클래스를 참조 변수형으로 가져다 쓰기 위해서는           
1. 멤버 변수를 선언할 때 해당 클래스를 자료형으로 사용하여 변수를 선언한다.
2. 선언을 한다고 클래스가 만들어지는 것은 아니기 때문에, 생성자에서 참조 변수의 객체를 생성한다. 

<br>

### 2) 클래스 자료형 사용하기

#### Student 클래스에서 Subject 클래스의 멤버 변수를 사용하여 메소드 생성
```java 
package reference;

public class Student {
	
	int studentID;
	String studentName;
	Subject korean;
	Subject math;
	
	public Student(){
		korean = new Subject();
		math = new Subject();
	}
	
	public void setKorean(String name, int score)
	{
		korean.subjectName = name;
		korean.scorePoint = score;
	}
	
	public void setMath(String name, int score)
	{
		math.subjectName = name;
		math.scorePoint = score;
	}

}
```

<br>

#### Student 클래스에서 Subject 클래스의 메소드 사용하여 메소드 생성
```java 
package reference;

public class Subject {
	Point;String subjectName;
	int score;
	
	public String getSubjectName() {
		return subjectName;
	}
	public void setSubjectName(String subjectName) {
		this.subjectName = subjectName;
	}
	public int getScorePoint() {
		return scorePoint;
	}
	public void setScorePoint(int scorePoint) {
		this.scorePoint = scorePoint;
	}
	
}
```

```java 
package reference;

public class Student {

	int studentID;
	String studentName;
	Subject korean;
	Subject math;
	
	public Student(int studentID, String studentName){
		this.studentID = studentID;
		this.studentName = studentName;
		
		korean = new Subject();
		math = new Subject();
	}


	public void setKorean(String name, int score)
	{
		korean.setSubjectName(name);;
		korean.setScorePoint(score);;
	}
	
	public void setMath(String name, int score)
	{
		math.setSubjectName(name);;
		math.setScorePoint(score);
	}
	
	public void showStudentInfo()
	{
		int total = korean.getScorePoint() + math.getScorePoint();
		System.out.println(studentName + "학생의 총점은 " + total + "점 입니다 .");
	}
}
```
<br>

#### main 함수를 생성하여 위 코드의 실행 확인하기
```java
package reference;

public class StudentTest {

	public static void main(String[] args) {
		
		Student studentJames= new Student(100, "james");
		
		studentJames.setKorean("국어",100);
		studentJames.setMath("수학",100);
		
        Student studentKim = new Student(102, "Kim");
		
		studentKim.setKorean("국어", 70);
		studentKim.setMath("수학", 85);
		
		studentJames.showStudentInfo();
		studentKim.showStudentInfo();
	}
}
```

<br>

#### 참조자료형 다른 예시
```java
//Event.java
package referenceEx;

public class Event {
	String eventName;
	int try1;
	int try2;
	
	public Event(String name) {
		this.eventName=name;
	}
	
	public int getTry1() {
		return try1;
	}
	public void setTry1(int try1) {
		this.try1 = try1;
	}
	public int getTry2() {
		return try2;
	}
	public void setTry2(int try2) {
		this.try2 = try2;
	}
	
}
```

```java
//Member.java
package referenceEx;

public class Member {
	
	String memberName;
	int memberID;
	Event soccer;
	Event basketball;
	
	public Member(String name, int ID){
		
		this.memberName=name;
		this.memberID=ID;
		
		soccer=new Event("축구");
		basketball=new Event("농구");
	}
	
	public void setSoccer(int score1, int score2) {
	    soccer.setTry1(score1);
		soccer.setTry2(score2);
		
	}
	
	public void setBasketball(int score1, int score2) {
	    basketball.setTry1(score1);
		basketball.setTry2(score2);
	}
		
	
	public void showMembersInfor() {
		int try1Total=soccer.getTry1()+basketball.getTry1();
		int try2Total=soccer.getTry2()+basketball.getTry2();
		System.out.println("이름: "+memberName+ ", ID: "+memberID+", 시도1_총점:"+ try1Total+ ", 시도2_총점: "+try2Total);
	}
	
}
```

```java
//MemberTest.java

package referenceEx;

public class MemberTest {

	public static void main(String[] args) {
		
		Member member1=new Member("park",10);
		Member member2=new Member("Kim",15);
		
		member1.setSoccer(70, 90);
		member1.setBasketball(100, 50);
		
		member2.setSoccer(85, 100);
		member2.setBasketball(80, 80);

		member1.showMembersInfor();
		member2.showMembersInfor();
	}
}
```

## 7. 정보 은닉

### 1) 접근 제어자
객체 지향 프로그램에서는 예약어를 사용해 클래스 내부의 변수나 메서드, 생성자에 대한 접근 권한을 지정할 수 있다.

* public: 외부 클래스에서 접근이 가능하며, 외부 클래스가 사용할 수 있다.
* private: 외부 클래스에서 사용할 수 없으며 해당 클래스에서만 사용할 수 있다.
* 아무 것도 없는 경우: default 이며 같은 패키ㅣㅈ 내부에서만 접근할 수 있다.

<br>

### 2) privite 변수에 접근하는 방법
get(), set() 메서드를 통해서 접근할 수 있다.
```java

package hiding;

public class Student {
	
	int studentID;
	private String studentName;
	int grade;
	String address;
	
	public String getStudentName() {
		return studentName;
	}

	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}

}
```
```java
package hiding;

public class StudentTest {

	public static void main(String[] args) {
		Student studentLee = new Student();
		studentLee.setStudentName("Park");
		System.out.println(studentLee.getStudentName());
	}
}
```

<br>

### 3) 정보 은닉
클래스 내부에서 사용할 변수나 메서드를 private로 선언해서 외부에서 접근하지 못하도록 하는 것.        
외부에서 접근하지 못하도록 하는 이유: 정보의 오류가 발생할 수 있기 때문이다.

```java
public class clock{
	public int time;
	public int min;
}

public static void main(String[] args){
	time=31;
	min=90;
}
```
 위와 같이 누군가가 시계에 접근해서 존재하지않는 31시간 90분 이라고 입력하게 되면 문제가 생길 것이다.  때문에 외부에서 누군가가 접근하지 못하게 정보 은닉이 필요하다. 따라서 접근 제어자를 public -> private로 변경하고 오류가 발생하면 해당 변수에 접근하지 못하도록 코드를 작성하면 오류를 막을 수 있다.


 ```java
public class clock{
	private int time;
	private int min;
    
  public setTime(int time){
    	if(time<0 || time>23){
        	system.out.println("시간 오류입니다.");
    	}else{
        	this.time = time;
        }
    }
  public setMin(int min){
    	if(min<0 || min>59){
        	system.out.println("분 오류입니다.");
    	}else{
        	this.min = min;
        }
    }
}
```


