# 기본 클래스

## 1. Object 클래스

### 1) Object 클래스란?
java.lang 패키지에는 기본적으로 많이 사용하는 클래스들이 포함되어 있는데, 이 패키지는 컴파일 할때 자동으로 추가된다.   그 중, Object 클래스는 모든 자바 클래스의 최상위 클래스이며, 모든 클래스는 Object 클래스로부터 상속을 받는다.  Object 클래스는 컴파일 과정에서 자동으로 추가된다. 아래 설명되는 모든 메서들은 Object 클래스의 메서드이다.

<br>

### 2) toString() 메서드

객체 정보를 문자열로 바꿔주는 역할을 한다. 재정의 하지 않은 toString() 메서드의 원형은 인스턴스 클래스 이름과 주소값을 보여준다. toString()은 System.out.println() 출력문에 참조 변수를 넣으면 자동으로 호출된다.

```java
//toStirng 원형
getClass().getName() +@+ Integer.toHexString(hashCode())
```

<br>

재정의되지 않았을 때
```java
package object;

   class Book {
	
	int bookNumber;
	String bookTitle;
	
	public Book(int bookNumber, String bookTitle ){
		this.bookNumber=bookNumber;
		this.bookTitle=bookTitle;
	}


	public class ToStringEx{
		public static void main(String[] args) {
			Book book1= new Book(200, "개미");
			String str = new String("Test");
			
			System.out.println(book1); //Object.Book@506e1b77  -> 클래스 이름과 주소 출력
			System.out.println(str);  //Test  -> String Class에서는 toString()이 이미 재정의되어있다.
		}		
	}
}
```
 
 <br>

직접 재정의
 ```java
 package object;

    class Book {
	
	int bookNumber;
	String bookTitle;
	
	public Book(int bookNumber, String bookTitle ){
		this.bookNumber=bookNumber;
		this.bookTitle=bookTitle;
	}


	@Override
	public String toString() {
		return bookNumber +", "+bookTitle; 
	}


	public class ToStringEx{
		public static void main(String[] args) {
			Book book1= new Book(200, "개미");;
			
			System.out.println(book1);  //200, 개미  -> 재정의하였기 때문에 bookNumber, bookTitle 출력 
			System.out.println(book1.toString());  //200, 개미
		}		
	}
}
 ```

 <br>

 ### 2) equals() 메서드
 두 인스턴스의 주소를 비교하여 같으면 true 다르면 false를 반환한다. 즉, '=='와 같다. 두 인스턴스의 모든 데이터는 같지만 주소가 다른 경우에는 기본적으로 False를 반환하기 때문에, 두 인스턴스가 같은 경우 True를 반환하기 위해서는 재정의를 해주어야 한다.

 <br>
 
 재정의 되지 않았을 때
 ```java
  package object;

    class Book {
	
	int bookNumber;
	String bookTitle;
	
	public Book(int bookNumber, String bookTitle ){
		this.bookNumber=bookNumber;
		this.bookTitle=bookTitle;
	}

	public class EqualsEx{
		public static void main(String[] args) {
			
			Book book1= new Book(200, "개미");
			Book book2= new Book(200, "개미")	;		
			String str1= new String("Test");
			String str2= new String("Test");
		
			System.out.println(book1==book2);  //false
			System.out.println(book1.equals(book2));   //false
			System.out.println(str1==str2);  //false
			System.out.println(str1.equals(str2));  //true  -> String class에서 이미 재정의됨
		}		
	}
}
  ```

  <br>

  직접 재정의
  ```java
  package object;

   class Book {
	
	int bookNumber;
	String bookTitle;
	
	public Book(int bookNumber, String bookTitle ){
		this.bookNumber=bookNumber;
		this.bookTitle=bookTitle;
	}
	
	@Override
	public boolean equals(Object obj) {
		
		if(obj instanceof Book) { //매개변수가 Object형 클래스이므로 다운캐스팅 해줘야 함
			Book book = (Book)obj;
			
			if(this.bookNumber == book.bookNumber) { //책 번호가 같을 경우 같은 책
				return true;
			}
			else
				return false;
			}
			return false;
	}
	
	public class EqualsEx{
		public static void main(String[] args) {
			
			Book book1= new Book(200, "개미");
			Book book2= new Book(200, "개미")	;		
		
			System.out.println(book1==book2);  //false
			System.out.println(book1.equals(book2));   //true

		}		
	}
}

  ```

  <br>

### 3) hashCode 메서드
Java의 Hash Code란, 객체를 식별할 수 있는 유니크한 값을 말한다. 따라서 hashCode 메서드는 객체의 고유한 값을 반환하며, 원형 hashCode는 인스턴스 주소를 반환한다. 만약, equals()에서 논리적으로 같은 객체도 같은 객체로 재정의했다면 hashCode도 마찬가지로 재정의해주어야 한다. 

<br>

String과 Integer 클래스의 hashCode 메서드  
  ```java
package object;

import java.util.Date;

public class HashCodeTest {

	public static void main(String[] args) {

		String str1 = new String("abc");
		String str2 = new String("abc");
		
		System.out.println(str1.hashCode());  //96354
		System.out.println(str2.hashCode());  //96354
		
		Integer i1 = new Integer(100);
		Integer i2 = new Integer(100);
		
		System.out.println(i1.hashCode());  //100
		System.out.println(i2.hashCode());  //100
		
	}
}
  ```
  String 클래스는 같은 문자열을 가진 경우 동일한 해시코드 값을 반환하고, Integer 클래스는 정수값을 반환하도록 재정의되어있다.

  <br>
위 Book 클래스에서 equals를 재정의 할 때 책 번호가 같으면 true를 반환하도록 하였기 때문에, hashCode()를 재정의 할 때도 책 번호를 반환하도록 하는 것이 가장 합리적이다.

  ```java
package object;

class Book {
	
	int bookNumber;
	String bookTitle;
	
	public Book(int bookNumber, String bookTitle ){
		this.bookNumber=bookNumber;
		this.bookTitle=bookTitle;
	}

	
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		return bookNumber;
	}

	public class HashCodeEx{
		public static void main(String[] args) {
			
			Book book1= new Book(200, "개미");
			Book book2= new Book(200, "개미")	;		

			// 재정의한 hashCode 출력
			System.out.println(book1.hashCode());   //200
			System.out.println(book2.hashCode());   //200
			
			// 실제 주소값 출력
			System.out.println(System.identityHashCode(book1));  //1349393271
			System.out.println(System.identityHashCode(book2));  //1338668845

		}		
	}
}
```

<br>

  ### 4) clone 메서드
  clone()은 인스턴스를 간단하게 복사하는 역할을 한다.

  ```java
package object;

class Point{
	int x;
	int y;
	
	public Point(int x, int y) {
		this.x=x;
		this.y=y;
	}
	
	public String toString() {
		return "x= "+x+", "+"y= "+y;
	}
}

class Circle implements Cloneable{  //객체를 복사해도 된다는 의미로 Cloneable을 구현 해야함
	Point point;
	int radius;
	
	public Circle(int x, int y, int radius){
		this.radius=radius;
		point = new Point(x,y);
	}
	
	public String toString() {
		return "원점은 "+ point + "이고, "+"반지름은 "+radius+"입니다."; 
	}

	@Override
	protected Object clone() throws CloneNotSupportedException {
		return super.clone();
	}	
	
}

public class ObjectClassTest {
	public static void main(String[] args) throws CloneNotSupportedException {
		Circle circle = new Circle(10, 20, 30);
		Circle copyCircle=(Circle)circle.clone();
		
		System.out.println(circle);  //원점은 x= 10, y= 20이고, 반지름은 30입니다.
		System.out.println(copyCircle);  //원점은 x= 10, y= 20이고, 반지름은 30입니다.
		System.out.println(System.identityHashCode(circle)); //1338668845
		System.out.println(System.identityHashCode(copyCircle));  //159413332
	}
}
  ```

  <br>

  ## 2. String 클래스

  ### 1) Stirng 클래스를 선언하는 2가지 방법
```java
String str1 = new String ("abc");
String str2 = "test";
```
* new 예약어를 사용하여 객체를 생성하는 경우 "abc" 메모리가 할당되고 새로운 객체가 생성된다, 따라서 Stirng str3 = new String("abc")를 생성하는 경우 다른 메모리가 또 할당된다. 
* str2 = "test" 와 같이 생성자르를 이용하지 않고 바로 문자열 상수를 가리키는 경우에는 str2가 기존에 만들어져 있던 "test"라는 문자열 상수 메모리 주소를 가리키게 된다. 따라서, String str4 = "test" 코드를 작성하면 str2와 str4의 주소는 같게 된다.

<br>

주소값 비교하기
```java
package string;

public class StringTest1 {

	public static void main(String[] args) {

		String str1 = new String("abc");
		String str2 = new String("abc");
		
		System.out.println(str1 == str2);    //false
		System.out.println(str1.equals(str2)); //true
	
		String str3 = "abc";
		String str4 = "abc";
	
		System.out.println(str3 == str4);  //true
		System.out.println(str3.equals(str4)); //true
	}
}
```

<br>

### 2) 문자열 연결하기
String 클래스는 한 번 생성된 문자열은 변경되지 않도록 final로 선언되어 있다. 따라서 문자열을 연결하면 둘 중 하나의 문자열이 변경되는 것이 아니라 두 문자열이 연결된 새로운 문자열이 생성된다.
```java
package string;

public class StringTest2 {

	public static void main(String[] args) {

		String javaStr = new String("java");
		String androidStr = new String("android");
		System.out.println(javaStr);  //java
		System.out.println(System.identityHashCode(javaStr));  //304736495
		
		javaStr = javaStr.concat(androidStr); //java 와 android 문자열의 연결
		
		System.out.println(javaStr);  //javaandroid
		System.out.println(System.identityHashCode(javaStr));  //430572844
	}
}
```

<br>

String 클래스를 사용하여 문자열을 계속 연결하면 메모리가 많이 낭비되기 때문에 이 문제를 해결하는 것이 바로 StringBuffer와 StringBuilder이다. 이 두 클래스는 문자열을 연결하면 기존에 사용하던 char[] 배열이 확장되므로 추가 메모리를 사용하지 않는다.
```java

package string;

public class StringBuilderTest {

	public static void main(String[] args) {
		
		String javaStr = new String("Java");
		System.out.println("javaStr 문자열 주소 :" +System.identityHashCode(javaStr)); //385242642
		
		StringBuilder buffer = new StringBuilder(javaStr); //String으로 부터 StringBuilder생성
		System.out.println("연산 전 buffer 메모리 주소:" + System.identityHashCode(buffer));  //824009085
		buffer.append(" and");                // 문자열 추가
		buffer.append(" android");            // 문자열 추가
		buffer.append(" programming is fun!!!"); //문자열 추가
		System.out.println("연산 후 buffer 메모리 주소:" + System.identityHashCode(buffer));  //824009085
		
		javaStr = buffer.toString(); //String 클래스로 반환
		System.out.println(javaStr);
		System.out.println("새로 만들어진 javaStr 문자열 주소 :" +System.identityHashCode(javaStr)); //2005857771
	}
}
```

<br>

## 3. Wrapper 클래스
기본 자료형처럼 사용할 수 있는 클래스  
ex) 정수를 사용할 때 기본형인 int 대신 객체형 Integer를 사용한다.
<img src="https://mblogthumb-phinf.pstatic.net/MjAxNzA0MDRfMTIy/MDAxNDkxMzA1MzQ1NTQ3.pKAL0ecx5r8d7IVXTU0l1HipVWazjjPUqPS8ZtAP9l4g.suNp1PNSNt_HXz-6gHMeqmJY_ajV7pNm7xP-hZbkXCgg.PNG.heartflow89/image.png?type=w800"></img>


<br>

### 4. Class 클래스
#### 1) Class 클래스란?
자바의 모든 클래스와 인터페이스는 컴파일이 되고 나면 class 파일로 생성된다. Class 클래스는 컴파일 된 class 파일에 저장된 클래스나 인터페이스 정보를 가져오는 데 사용한다. 따라서 클래스 정보를 직접 찾아야 할 경우 사용된다.

<br>

#### 2) Class 클래스 사용 방법
1. Object 클레스의 getClass()메서드 사용
```java
String s - new String();
Calss C = s.getClass();
```

2. 클래스 파일 이름을 Class 변수에 직접 대입하기
```java
Class C = String.Class;
```

3. Class.forName("클래스 이름")메서드 사용하기
```java
Class C = Class.forName("java.lang.String")
```

<br>

### 3. Class.forName()을 사용해 동적 로딩하기
forName()메서드를 사용하여 Class 크래스를 가져올 떄 가장 유의해야할 점은 해당 forName("클래스이름")의 클래스 이름이 문자열 값이므로, 문자열에 오류가 있어도 컴파일할 때 그 오류를 알 수 없다. 하지만, 여러 클래스 중 하나를 선택한다거나, 시스템 연동 중 매개변수로 넘어온 값에 해당하는 클래스가 로딩되고 실행하는 경우에는 동적 로딩 방식을 유연하게 사용할 수 있다.