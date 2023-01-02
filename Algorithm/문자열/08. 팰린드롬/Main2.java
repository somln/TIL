import java.util.Scanner;

public class Main2 {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.nextLine();
		String answer ="NO";
		
		s=s.toUpperCase().replaceAll("[^A-Z]",""); //A~Z가 아닌 문자를 없애기
		String temp = new StringBuilder(s).reverse().toString();
		
		if(s.equals(temp)) {
			answer="YES";
		}

		System.out.println(answer);
		
		in.close();	
	}
}