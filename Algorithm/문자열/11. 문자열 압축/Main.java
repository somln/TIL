import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.next();
		char pre=s.charAt(0);
		int count=1;
		
		for(int i=1; i<s.length(); i++){
			//이전 문자와 같으면 count 증가
			if(pre==s.charAt(i)) {
				count++;
			}
			else {
				//이전 문자와 다르면 문자, count 출력
				System.out.print(pre);
				if(count!=1) System.out.print(count);
				//pre와 count 변경
				pre=s.charAt(i);
				count=1;
			}
		}
		//마지막 문자는 출력되지 않으므로 따로 코드로 작성
		System.out.print(pre);
		if(count!=1) System.out.print(count);

		in.close();	
	}
}
