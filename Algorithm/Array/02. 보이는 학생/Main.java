import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int max=0;
		int count=0;
		
		for(int i=0; i<N; i++) {
			int x=in.nextInt();
			if(x>max) {
				max=x;
				count++;
			}
		}
		System.out.println(count);
 	    in.close();
	}
}
