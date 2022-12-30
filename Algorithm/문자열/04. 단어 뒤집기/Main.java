import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		String[] str = new String[n];
		ArrayList<String> answer = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			str[i]=in.next();
		}
		
		for(String s :str) {
			String temp = new StringBuilder(s).reverse().toString();
			answer.add(temp);
		}
		
		for(String s : answer) {
			System.out.println(s);
		}

		in.close();	
	}
}

/*
 * String은 문자를 수정하면 새로운 객체가 만들어지지만, StringBuilder는 기존 객체가 수정되기 때문에 
   StringBuilder를 사용한다
 * StringBuilder를 사용한 후에는, toString을 호출해  String형으로 반환해주어야 한다.  
*/

/*
ArrayList를 사용하지 않고,

String[] answer = new String[n];
for(int i=0; i<n; i++) {
  String temp = new StringBuilder(str[i]).reverse().toString();
  answer[i] = temp;
}

도 가능하다.
*/
