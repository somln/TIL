import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.next();
		int answer=0;
		
		s=s.replaceAll("[^0-9]","");
		for(char x:s.toCharArray()) {
			answer=answer*10+x-'0';
		}
		
		System.out.println(answer);
		
		in.close();	
	}
}

/* 
 * char형인 숫자를 int형 숫자로 바꿀 때, 0의 아스키코드 혹은 '0'을 빼주면 됨
 * 하나의 문자만 바꾸는 것이 아니라 여러개를 자연수로 만들어야 하므로 곱하기 10을 해서 밀어줌
 */