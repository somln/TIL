import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s1 = in.next();
		//s1을 뒤집어서 s2와 비교
		String s2= new StringBuilder(s1).reverse().toString();

		//equalsIgnoreCase: 대소문자 구분X
		if(s1.equalsIgnoreCase(s2)) {
			System.out.println("YES");
		}
		else {
			System.out.println("NO");
		}
		
		in.close();	
	}
}