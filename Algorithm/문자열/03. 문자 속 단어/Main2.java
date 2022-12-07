import java.util.Scanner;

public class Main2 {
   public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    String str = in.nextLine();
    String answer="";
    String temp="";
    int max=0;
    int pos;
    
    while((pos=str.indexOf(" "))!=-1) { //공백 위치를 pos에 저장

        temp=str.substring(0,pos);  //temp에 공백을 기준으로 단어를 잘라서 저장
        if(max>temp.length()) {   
            answer=temp;
        }
        str=str.substring(pos+1);  //공백 이후의 단어 str에 저장 
    }
    if(str.length()>max) {  //마지막 단어는 temp에 저장되지 않기 때문에 따로 확인해야함
        answer=str;
    }
    
    System.out.println(answer);
    in.close();	
    
   }
}
