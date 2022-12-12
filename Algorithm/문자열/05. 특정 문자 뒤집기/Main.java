import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s = in.next();
		char[] str = s.toCharArray();
		
		int lt=0;
		int rt=str.length-1;
		
		while(lt<rt) {
			if(!Character.isAlphabetic(str[lt])) lt++;
			else if(!Character.isAlphabetic(str[rt]))rt--;
			else {
				char temp=str[lt];
				str[lt]=str[rt];
				str[rt]=temp;				
			    lt++;
			    rt--;
			}
		}
		
		String answer = String.valueOf(str);
		System.out.println(answer);
		
		in.close();	
	}
}
