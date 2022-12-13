import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String s = in.next();
		String answer="";
		
		for(int i=0; i<s.length(); i++) {
			if(s.indexOf(s.charAt(i))==i){
				answer+=s.charAt(i);
			}
		}
		
		System.out.println(answer);
		in.close();	
	}
}