import java.util.Scanner;

public class Main2 {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.next();
		int answer=0;
		
		s=s.replaceAll("[^0-9]","");  //숫자만 추출해서
		answer=Integer.parseInt(s);  //문자열을 숫자로 변환

		System.out.println(answer);
		
		in.close();	
	}
}