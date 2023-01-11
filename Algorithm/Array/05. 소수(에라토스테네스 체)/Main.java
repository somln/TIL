import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] check = new int[N+1];
		int count=0;
		
		for(int i=2; i<=N; i++) {
			if(check[i]==0) count++;
			for(int j=i; j<=N; j= j+i) check[j]=1;
		}
		
		System.out.println(count);
 	    in.close();
	}
}

