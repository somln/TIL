import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		String s = in.next();
		String result="";

		for(int i=0; i<n; i++){
			//앞에 문자 7개를 잘라서, #->1, *->0 으로 변환
			String temp=s.substring(0,7).replace('#', '1').replace('*','0');
			//문자열을 정수형으로 변환
			int num=Integer.parseInt(temp,2);
			//int형을 char형으로 저장
			result=result+=(char)num;
			//앞에 문자 7개 버리기
			s=s.substring(7);
		}
		System.out.println(result);
	
		in.close();	
	}
}
