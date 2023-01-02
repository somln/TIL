import java.util.Scanner;

public class Main2 {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.next();
		char c = in.next().charAt(0);
		int[] answer = new int[s.length()];
		int dis =1000;
		
		//해당 값보다 왼쪽에 있는 e로부터의 거리 구하기
		for(int i=0; i<s.length(); i++) {
			if(s.charAt(i)==c) dis=0;
			else dis++;
			answer[i]=dis;
		}
		
		//해당 값보다 오른쪽에 있는 e로부터의 거리 구해서 더 작은 값 저장하기
		 dis =1000;
		for(int i=s.length()-1; i>=0; i--) {
			if(s.charAt(i)==c) dis=0;
			else dis++;
			if(answer[i]>dis) answer[i]=dis;
		}
		
		for(int x:answer) {
			System.out.print(x+" ");
		}
		
		in.close();	
	}
}
