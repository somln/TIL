import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s = in.next();
		char key= in.next().charAt(0);
		int count=0;
		
		in.close();
		s=s.toLowerCase();
		key=Character.toLowerCase(key);
		
		for(int i=0; i<s.length(); i++) {
			
			if(s.charAt(i)==key) {
				count++;
			}
		}
		System.out.println(count);	
	}
}