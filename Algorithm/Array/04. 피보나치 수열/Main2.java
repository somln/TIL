import java.util.Scanner;

public class Main2 {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int a=1;
		int b=1;
		System.out.print(a+" "+b+" ");
		for(int i=2; i<N; i++) {
			int c=a+b;
			System.out.print(c+" ");
			a=b;
			b=c;
		}

 	    in.close();
	}
}