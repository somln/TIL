import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] number = new int[N];
		
		for(int i=0; i<N; i++) {
			int x=in.nextInt();
			number[i]=x;
		}
		
		System.out.print(number[0]+" " );
		
		for(int i=1; i<N; i++) {
			if(number[i]>number[i-1]) {
				System.out.print(number[i]+ " ");
			}
		}
 	    in.close();
	}
}
