import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] A = new int[N];
		int[] B = new int[N];
		char[] answer = new char[N];
		
		for(int i=0; i<N; i++) {
			A[i]=in.nextInt();
		}
		
		for(int i=0; i<N; i++) {
			B[i]=in.nextInt();
		}
		
		for(int i=0; i<N; i++) {
			if(A[i]==B[i]) answer[i]='D';
			else if((A[i]==1)&&(B[i]==2)) answer[i]='B';
			else if((A[i]==2)&&(B[i]==3)) answer[i]='B';
			else if((A[i]==3)&&(B[i]==1)) answer[i]='B';
			else answer[i]='A';
		}
		
		for(char a:answer) {
			System.out.println(a);
		}
		
 	    in.close();
	}
}