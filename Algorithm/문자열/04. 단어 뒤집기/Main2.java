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
		
		for(String s:str) {
			//문자열을 배열로
			char[] x=s.toCharArray();
			int lt=0;
			int rt=x.length-1;
			while(lt<rt) {
				char temp=x[lt];
				x[lt]=x[rt];
				x[rt]=temp;
				lt++;
				rt--;
			}
			//배열을 문자열로
			String tempS =String.valueOf(x);
			answer.add(tempS);
		}
		
		for(String s : answer) {
			System.out.println(s);
		}

		in.close();	
	}
}