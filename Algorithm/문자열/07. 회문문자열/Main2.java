import java.util.Scanner;

public class Main2 {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s = in.next();
		s=s.toUpperCase();
		String answer = "YES";
		
        //문자열을 반으로 잘라서 대칭인지 비교
		for(int i=0; i<s.length()/2; i++) {
			if(s.charAt(i)!=s.charAt(s.length()-1-i)) {
				answer="NO";
				break;
			}
		}
		System.out.println(answer);
		in.close();	
	}
}
