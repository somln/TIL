import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] f = new int[N];
		f[0]=1;
		f[1]=1;
		
		for(int i=2; i<N; i++) {
			f[i]=f[i-1]+f[i-2];
		}
		
		for(int x:f) {
			System.out.print(x+" ");
		}
		
 	    in.close();
	}
}
