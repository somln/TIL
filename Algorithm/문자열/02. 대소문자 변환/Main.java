import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s = in.next();
		char t;
		char t2;
		
		for(int i=0; i<s.length(); i++) {
			t=s.charAt(i);
			if(Character.isUpperCase(t)) {
				t2=Character.toLowerCase(t);
			}
			else {
				t2=Character.toUpperCase(t);
			}
			System.out.print(t2);
	   }
		in.close();
	}
}
