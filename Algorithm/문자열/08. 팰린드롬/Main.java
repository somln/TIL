import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		ArrayList<Character> newStr = new ArrayList<Character>();		
		
		String s = in.nextLine();
		char[] str = s.toCharArray();
		String answer ="YES";
		
		for(char c:str) {
		if(Character.isAlphabetic(c)) {
			Character.toLowerCase(c);
			newStr.add(Character.toLowerCase(c));
		   }
		}
		
		for(int i=0; i<newStr.size()/2; i++) {
			if(newStr.get(i)!=newStr.get(newStr.size()-1-i)) {
				answer = "NO";
				break;
			}
		}
		
		System.out.println(answer);
		
		in.close();	
	}
}