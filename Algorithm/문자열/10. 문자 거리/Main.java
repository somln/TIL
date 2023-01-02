import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
				
		String s = in.next();
		char c = in.next().charAt(0);
		ArrayList<Integer> indexList = new ArrayList<>();
		ArrayList<Integer> resultList = new ArrayList<>();
		int index = s.indexOf(c);
		
		//indexList에 해당 문자가 위치한 모든 인덱스 저장		
		while(index != -1) {
			indexList.add(index);
			index=s.indexOf(c,index+1);
		}
		
		//인덱스 별로 indexList에 저장된 인덱스들과 빼기 연산을 하여 최솟값 저장
		for(int i=0; i<s.length(); i++) {
			int min= 100;
			int temp =0;
			for(int x:indexList) {
				
				temp= Math.abs(i-x);
				if(min>temp) min=temp;
			}
			resultList.add(min);
		}
		
		//결과 출력
		for(int result: resultList) {
			System.out.print(result+ " ");
		}
		in.close();	
	}
}