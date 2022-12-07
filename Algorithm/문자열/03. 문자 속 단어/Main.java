import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		String str = in.nextLine();
		String[] array = str.split(" ");
		int max=0;
		String answer = null;
		
		for(String s:array ) {
			if(s.length()>max) {
				max= s.length();
				answer=s;
			}
		}
		System.out.println(answer);
		in.close();	
	}

}