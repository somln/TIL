#####-주석처리-#####
'''이렇게
하면
여러문장이
주석 처리'''

#####-변수-#####
#숫자,문자 자료형
name="해피"
animal="고양이"
age=4
hobby="낮잠"
#boolean 자료형
is_adult=age>=3


print("우리집 강아지 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 졸아해요")
print("연탄이는 어른일까요? True")

hobby="공놀이"
print("우리집 "+animal+" 이름은 "+name+"이예요")
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 졸아해요")
print(name+"는 어른일까요? "+str(is_adult))

print("우리집 ",animal," 이름은 ",name,"이예요")
print(name,"는 ",age,"살이며, ",hobby,"을 아주 졸아해요")
print(name,"는 어른일까요? ",is_adult)

#Quiz)

station="사당"
print(station+"행 열차가 들어오고 있습니다.")
station="신도림"
print(station+"행 열차가 들어오고 있습니다.")
station="인천공항"
print(station+"행 열차가 들어오고 있습니다.")

#####-연산자-#####
print(3-2)
print(2*5)
print(6/3)
print(2**3) #제곱
print(5%3)  #나머지
print(5//3) #몫
print(10<=3) #False
print(10>=3) #Ture
print(3==3)
print(4==2)
print(3+4==7)

print(1!=3)
print(not (1!=3))

print((3>0)and(3<5)) #True
print((3>0)&(3<5)) #True
print((3>0)or(3>5)) #True
print((3>0)|(3>5)) #True
print(5>4>3) #True
print(5>4>7) #False

#####-간단한 수식-#####
print(2+3+4)  #9
print((2+3)*4) #20

number=2+3+4
print(number)
number=number+2
number+=2
print(number)
number*=2
number-=2
number%=2
print(number)

#####-숫자처리함수-#####
print(abs(-5)) #절대값
print(pow(4,2)) #4의 2승
print(max(5,12)) #최댓값
print(min(5,12)) #최솟값
print(round(3.14)) #반올림

#####-랜덤함수-#####
from random import*

print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
print(random()*5) #0.0~5.0미만의 임의의 값 생성
print(int(random()*10)) #0.0~10 미만의 임의의 값 생성
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
print(randrange(1,46)) #1~46 미만의 임의의 값 생성
print(randint(1,45)) #1~45 이하의 임의의 값 생성

#Quiz
from random import*
day=(randint(4,28))
print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 선정되었습니다.")

#####-문자열-#####
sentence='나는 소년입니다'
print(sentence)
snetence2="파이썬은 쉬워요"
print(snetence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#####-슬라이싱;원하는 값만큼 가져옴-#####
jumin="010730-1234567"
print("성별: "+jumin[7])
print("연: "+jumin[0:2]) #=0부터 2 직전까지
print("월: "+jumin[2:4])
print("일: "+jumin[4:6])
print("생년월일: "+jumin[:6]) #처음부터 6 직전까지
print("뒤 일곱자리: "+jumin[7:]) #7부터 끝까지
print("뒤 일곱자리 (뒤에서부터):" +jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#####-문자열 처리 함수-#####
python="Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #첫번째 글자가 대문자인지
print(len(python)) #문자열 개수 세기
print(python.replace("Python","Java")) #문자열 바꾸기 (Python을 Java로)

index=python.index("n") #n이 몇번 째에 있는 지
print(index)
index=python.index("n",index+1) #앞에서 찾은 위치 다음 위치부터 n이 몇 번째에 있는지=2번째 n 위치
print(index)

print(python.find("n")) #index함수와 비슷한 기능
print(python.find("w")) #문자열에 없는 문자를 찾을 때는 -1 출력
print("hi")
#print(python.index("w")) #문자열에 없는 문자를 찾을 때는 오류

print(python.count("n")) #변수에서 n이 총 몇번 등장

#####-문자열 포멧-#####
print("a"+"b")
print("a","b")

#방법 1
print("나는 %d살 입니다" %20)
print("나는 %s을 좋아해요." %"파이썬")
print("Apple은 %c로 시작해요." %"A")
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법 3
print("나는 {age}살 이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법 4
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#####-탈출문자######
# \n: 줄바꿈
print("백문이불여일견\n 백견이 불여일타")

# \"문자열"\: "까지 같이 출력
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\: 문장 내에서는 \
print("C:\\Users\\USER\\Desktop\\pythonWorkspace>")

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine") 
#Red Apple을 출력 후 커서를 맨 앞으로 이동해서 다시 Pine을 쓰기 때문에 PineApple출력

# \b: 백스페이스(한 글자 삭제)
print("Redd\bApple") #=RedApple

# \t: 탭
print("Red\tApple") #=Red   Apple

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

url="http://naver.com"
url="http://google.com"
url="http://youtube.com"

ex=url[7:] 
ex=ex[:-4]
ex1=ex[:3]
len=len(ex)
ecount=ex.count("e")
print(f"생성된 비밀번호: {ex1}{len}{ecount}!")

url="http://naver.com"
ex=url.replace("http://","")
ex=ex[:ex.index(".")]
print(ex)
'''password=ex[:3]+str(len(ex))+str(ex.count("e"))+"!"
print("생성된 비밀번호: {}"format(password))'''

#####-리스트[]-#####
subway=[10, 20, 30]
print(subway)

subway=["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호")) #=1

subway.append("하하") #하하를 리스트 마지막
print(subway)

subway.insert(1,"정형돈") #1번째 인덱스에 정형돈 넣기
print(subway)

print(subway.pop()) #리스트 마지막순서 제거, 제거되는 값 출력 =하하
print(subway)

print(subway.pop()) #리스트 마지막순서 제거, 제거되는 값 출력 =박명수
print(subway)

print(subway.pop()) #리스트 마지막순서 제거, 제거되는 값 출력 =조세호
print(subway)

subway=["유재석","정형돈","조세호","박명수","유재석"]
print(subway.count("유재석")) #유제석이 몇 번 나오는지

num=[5,2,3,1,4]
num.sort() #순서대로 정렬
print(num)

num.reverse()
print(num) #역정렬

num.clear() #리스트 비움
print(num) 

num=[5,2,3,1,4]

#다양한 자료형과 함께 사용 가능
mix=["조세호",20,True]
print(mix)

#리스트 확장
num.extend(mix)
print(num)

#####-사전{:}-#####
cabinet={3:"유재석",100:"김태호"}

#사전 자료형 출력
print(cabinet[3]) #=유재석
print(cabinet[100]) #=김태호
print(cabinet.get(3)) #=유재석
print(cabinet.get(100)) #=김태호

#print(cabinet[5]) #오류를 출력, 프로그램 종료
print("hi") #출력되지 않음 

print(cabinet.get(5)) #none 출력
print(cabinet.get(5,"사용 가능")) #5의 값이 없으면 사용가능 출력
print("hi") #hi출력

#사전 자료형에 값이 있는지?
print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet.get("B-100"))

#값 업데이트, 추가
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

#값 삭제
del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) #key 들만 출력
print(cabinet.values()) #value 들만 출력
print(cabinet.items()) #key, value 쌍으로 출력

cabinet.clear() #모든 값 삭제
print(cabinet)

#####-튜플(,,)-#####
#변경되지 않는 목록을 사용할 때

menu=("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

#menu.add("생선가스") 불가능

name="김종국"
age=20
hobby="코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#####-집합{,,}-#####
#중복 안됨, 순서 없음

my_set={1,2,3,3,3}
print(my_set)

java={"유재석", "김태호", "양세형"}
python=set(["유재석","박명수"])

#교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합(java 또는 python을 할 수 있는 개발자 )
print(java | python)
print(java.union(python))

#차집합(java는 할 수 있지만 python은 할 수 있는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊어버림
java.remove("김태호")
print(java)

#####-자료구조의 변경-######
#커피숍

#집합
menu={"커피", "우유", "주스"}
print(menu,type(menu))

#리스트로 변경
menu=list(menu)
print(menu,type(menu))

#튜플로 변경
menu=tuple(menu)
print(menu,type(menu))

#집합으로 변경
menu=set(menu)
print(menu,type(menu))

#Quiz 4
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
from random import*
shuffle(lst)
lst_w=sample(lst,4)

print("--당첨자 발표--")
print("치킨 당첨자: {}".format(lst_w[0]))
print("치킨 당첨자: [{}, {}, {}]".format(lst_w[1],lst_w[2],lst_w[3]))
print("--축하합니다--")


from random import*
users=list(range(1,21))
shuffle(users)
winners=sample(users,4)

print("--당첨자 발표--")
print("치킨 당첨자: {}".format(winners[0]))
print("치킨 당첨자: {}".format(winners[1:]))
print("--축하합니다--")

#####-if-#####
weather=input("오늘 날씨는 어때요? ")
#input():입력한 값을 문자열으로 저장
if weather=="비" or weather=="눈":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp=int(input("기온은 어때요?"))
if 30<=temp:
    print("너무 더워요. 나가지 마세요")
elif 10<=temp and temp<30:
    print("괜찮은 날씨에요")
elif 0<=temp<10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
    
#####-for-#####
for waitting_no in [0,1,2,3,4]:
    print("대기번호: {0}".format(waitting_no))

for waitting_no in range(1,6): #1,2,3,4,5
    print("대기번호: {0}".format(waitting_no))

starbucks=["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

#####-while-#####
customer="토르"
index=5
while index>=1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index)) 
    index-=1
    if index==0:
        print("커피는 폐기처분되었습니다.")

#무한루프
"""customer="아이언맨"
index=1
while True:
   print("{0}, 커피가 준비되었습니다. 호출:{1}회.".format(customer,index)) 
   index+=1  """

customer1="토르"
person="unknown"

while person!=customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person=input("이름이 어떻게 되세요?")

 #####-continue와 break-#####
absent=[2,5] #결석
no_book=[7] #책을 깜빡했음
for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue #아래에 있는 코드를 실행시키지 않고 다음 반복으로 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로".format(student))
        break #반복문을 빠져나옴
    print("{0},책을 읽어봐.".format(student)) 

#####-한줄 for-#####
#출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 ->101, 102, 103, 104
students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students=["Iron man", "Thor", "I ma groot"]
students=[len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students=["Iron man", "Thor", "I ma groot"]
students=[i.upper() for i in students]
print(students)

#Quiz)
from random import*
cnt=0
for i in range(1,51):
    time=randrange(5,51)
    if 5<=time<=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객: {0}분".format(cnt))

#####-함수-##### 
#전달값, 반환값X
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

#전달값, 반환값o
#입금
def deposit(balance, money): #balacne:잔액, money: 입금 금액
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance+money
balance=0
balance=deposit(balance,1000)
print(balance)

#출금
def withdraw(balance, money): #balacne:잔액, money: 출금 금액
    if balance>=money:
       print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))   
       return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance=withdraw(balance,2000)
balance=withdraw(balance,500)

#출금 수수료 추가
def withdraw_night(balacne, money):
    commission=100
    return commission, balance-money-commission #여러 개의 값 한번에 반환도 가능

commission, balance=withdraw_night(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

#####-기본값-#####
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용언어: {2}.".format(name, age, main_lang))

profile("우재석",20,"파이썬")
profile("김태호",25,"자바")

#같은 학교, 같은 학년, 같은 반, 같은 수업
def profile_d(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용언어: {2}.".format(name, age, main_lang))

#age와 main_lang이 기본값으로 설정되어 있기 때문에 name만 전달해도 OK
profile_d("우재석")
profile_d("김태호") 

#####-키워드값-#####
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유제석", main_lang="파이썬", age=20) 
profile(main_lang="자바", age=25, name="김태호") 
#함수를 호출할 때 매개변수의 값을 키워드를 이용하면 순서가 뒤섞여도 잘 전달됨.

#####-가변인자-#####
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")   #end=" "를 넣어주면 줄바꿈 X
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "SWift", "", "", "") 
#사용할 줄 아는 언어가 5개 보다 많으면 함수를 수정해야함

def profile_v(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")   #end=" "를 넣어주면 줄바꿈 X
    for lang in language:
        print(lang, end=" ")
    print()

profile_v("유재석", 20, "Python", "Java", "C", "C++", "C#", "ZavaScript")
profile_v("김태호", 25, "Kotlin", "SWift", "", "", "") 

#####-지역변수와 전역변수-#####
gun=10
#1
def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용 
    gun=gun-soldiers
    print("[함수 내]남은 총: {0}".format(gun))
    
print("전체 총: {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))

#2가 더 좋은 방법
def checkpoint_ret(gun, soldiers): #전역변수 gun을 매개변수로 받고 다시 반환
    gun=gun-soldiers
    print("[함수 내]남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
gun=checkpoint_ret(gun,2)
print("남은 총: {0}".format(gun))   

#Quiz 6 
height=175
gender="남자"

def std_weight(height, gender):
    if gender=="남자":
        return height*height*22
    else:
        return height*height*21
        
weight=round(std_weight(height/100, gender),2) #소숫점 둘 째자리 까지 표시
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender,weight ))

#####-표준입출력-#####
#sep, end
print("Python", "Java", "JavaScript", sep=" VS ") #sep는 , 자리에 들어갈 문자, 문자들을 구분하는 역할
print("Python", "Java", sep=",", end="?") #end:문장의 끝 부분을 물음표로 바꿈(줄바꿈 X)
print("무엇이 더 재밌을까요?")

#sys
import sys
print("Python", "Java", file=sys.stdout) #표준출력
print("Python", "Java", file=sys.stderr) #표준에러

#ljust, rjust
scores={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":") 
    #ljust(8):8칸을 확보한 후 왼쪽 정렬 rjust(4):4칸을 확보한 후 오른쪽 정렬

#zfill
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3)) #3개의 공간 중 빈 공간은 0으로 채움

#표준입력:input
answer=input("아무 값이나 입력하세요: ")
#사용자가 입력하고 엔터를 치면 그 값이 문자열 형태로 answer에 저장됨
print("입력하신 값은" +answer+"입니다.")

#####-다양한 출력 포멧-#####
#빈자리는 빈공간으로 두고, 오른쪽 정렬을하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
#3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000000000000))
#3자리마다 콤마를 찍어주기, +-표시하기
print("{0:+,}".format(-1000000000000000000000))
#3자리마다 콤마를 찍어주기, +-표시하기, 자릿수 확보하기, 빈자리는 ^표시
print("{0:^<+30,}".format(1000000000000))
#소숫점 출력
print("{0:f}".format(5/3))
#소숫점을 특정 자리수까지만 표시 (소수점 셋째자리에서 반올림)
print("{0:.2f}".format(5/3))

#####-파일 입출력-#####
##파일 쓰기##

score_file=open("score.txt","w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()
#score_file에 대한 변수를 만들고 open을 통해서 file을 열음
#파일이름:score.txt, 쓰기위한 목적으로 열음, encoding="utf8"을 정의해주지 않으면 한글이 이상한 문자로 적힐수 O
#파일을 쓰기 목적으로 열어서 파일에 내용을 쓰고 파일을 닫는 과정

score_file=open("score.txt","a",encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()
#어떤 내용이 존재하는 파일에 이어쓰기를 하고싶을 때는 "a"
#print문이 아닌 .write()를 사용하면 줄바꿈이 따로 없기 때문에 줄바꿈을 해주어야 함

##파일 읽기##

score_file=open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()
#파일의 내용을 읽어오는 목적으로 파일을 열음
#파일의 모든 내용을 출력

score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") 
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()
#줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()    
#줄 별로 읽고 다음 줄에 내용이 없을 경우 반복문 종료

score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines() 
for line in lines:
    print(line,end="")
score_file.close()    
#모든 line을 가져와서 list 형태로 저장 후 for문을 통해 출력

#파일 입출력 복습
menu_file=open("menu.txt","w",encoding="utf8")
print("아메리카노=1500", file=menu_file)
print("카페라떼=3500", file=menu_file)
menu_file.close()

menu_file=open("menu.txt","a",encoding="utf8")
menu_file.write("카페모카=4000")
menu_file.write("\n우유=1000")
menu_file.close

menu_file=open("menu.txt","r",encoding="utf8")
print(menu_file.read())
menu_file.close


menu_file=open("menu.txt","r",encoding="utf8")
print(menu_file.readline())
print(menu_file.readline())
print(menu_file.readline())
print(menu_file.readline())
menu_file.close

menu_file=open("menu.txt","r",encoding="utf8")
while True:
    line=menu_file.readline()
    if not line:
        break
    print(line,end="")
menu_file.close

menu_file=open("menu.txt","r",encoding="utf8")
lines =menu_file.readlines()
for line in lines:
    print(line,end="")
menu_file.close

#####-pickle-#####
#pickle을 이용하여 데이터를 파일 형태로 저장 -> pickle을 통해 파일에서 데이터를 가지고 올 수 있음
import pickle
profile_file=open("profile.pickle","wb")
profile={"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle","rb")
profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

####-with-#####
import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))
#profile.pickle 파일을 열어서 profile_file 변수에 저장하고, 파일 내용을 pickle.load를 통해서 불러와서 출력
#열었던 파일에 대해 close를 할 필요X

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부")

with open("study.txt","r",encoding="utf8") as study_file: 
    print(study_file.read())

#with를 사용하면 두 문장으로 간단하게(close 필요X) 파일을 읽고 쓸 수 있음 

#Quiz
for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("-{}주차 주간보고-\n".format(i))
        report_file.write("부서: \n")
        report_file.write("이름: \n")
        report_file.write("x업무 요약: -\n")

#####-클래스-#####
# 1. __init__
class imsi:
    def __init__(self):
        print("JSS 클래스 선언!")
    def show(self):
        print("show 실행!")   
#init: 클래스를 선언하는 순간 실행되는 함수
#a=imsi()를 선언하는 순간 __init__함수 안 내용이 실행됨 
#따라서 init에는 반드시 필요한 내용이 들어가게 됨

a=imsi() #선언 하는 순간 init안의 내용이 실행됨
a.show() #init 함수가 아닌 경우에는 만들어진 class 변수 뒤에 . 함수 이름을 붙여줘야 실행됨

# 2. self
class JSS:
    def __init__(self):
        self.name=input("이름: ")
        self.age=input("나이: ")
    def show(self):
        print("나이 이름은 {}, 나이는 {}세 입니다.".format(self.name, self.age))
#self는 클래스를 저장할 변수를 뜻함 #a.show에서 a를 의미    

b=JSS()
b.show()

# 3.상속
class JSS2(JSS):
    def __init__(self): #init함수를 다시 선언
        super().__init__() #JSS의 init함수를 그대로 가져옴
        self.gender=input("성별: ")
    def show(self):
        print("나이 이름은 {}, 성별은 {} 나이는 {}세 입니다.".format(self.name,self.gender, self.age))

c=JSS2()
c.show()       

#####-클래스-#####
class unit:
    def __init__(self, name, hp, damage):
        self.name=name #맴버 변수 초기화
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
        
marine1=unit("마린", 40, 5)
marine2=unit("마린", 40, 5)
tank=unit("탱크", 150, 5)

wraith1=unit("레이스", 80, 5)
print("유닛이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.hp))

wraith2=unit("빼앗은 레이스", 80, 5)
wraith2.clocking=True 
#클래스 외부에서 원하는 변수를 확장할 수 있음, 확장을 한 객채에만 적용되고 다른 객체에는 적용x

if wraith2.clocking==True:
    print("{0}는 현재 크로킹 상태입니다.".format(wraith2.name))   


#####-메소드-#####
#:클래스 안에 구현된 함수

#일반유닛
class unit:
    def __init__(self, name, hp, damage):
        self.name=name #맴버 변수
        self.hp=hp
        self.damage=damage

 #공격유닛       
class AttackUnit:
     def __init__(self, name, hp, damage):
        self.name=name #클래스 내에서 정의된 변수: 맴버 변수
        self.hp=hp
        self.damage=damage  

     def attack(self,locattion):
         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
             .format(self.name, locattion, self.damage))  
             #self는 자기자신을 의미, self.name을 통해 자기 자신의 변수에 접근 할 수 있음
             #self를 적지 않으면 전달 받은 값을 쓴다는 의미
    
     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp-=damage
         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
         if self.hp<=0:
             print("{0} : 파괴되었습니다.".format(self.name))

firebat1=AttackUnit("파이어뱃", 50, 16) #파이어벳의 공격력은 50, 데미지는 16
firebat1.attack("5시") #파이어뱃이 5시 방향으로 공격
firebat1.damaged(25) #파이어뱃이 25데미지를 공격 받음
firebat1.damaged(25) #파이어뱃이 25데미지를 공격 받음
     
#####-상속-#####
#:함수에서 겹치는 부분을 상속받음
#일반 유닛
class unit:
    def __init__(self, name, hp):
        self.name=name #맴버 변수
        self.hp=hp

 #공격유닛       
class AttackUnit(unit):
     def __init__(self, name, hp, damage):
         unit.__init__(self,name,hp) #unit의 init함수 상속
         self.damage=damage  #추가로 damage 정의 

     def attack(self,locattion):
         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
             .format(self.name, locattion, self.damage))  
             #self는 자기자신을 의미, self.name을 통해 자기 자신의 변수에 접근 할 수 있음
             #self를 적지 않으면 전달 받은 값을 쓴다는 의미
    
     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp-=damage
         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
         if self.hp<=0:
             print("{0} : 파괴되었습니다.".format(self.name))

#####-다중 상속-#####
#일반 유닛
class unit:
    def __init__(self, name, hp):
        self.name=name #맴버 변수
        self.hp=hp

 #공격유닛       
class AttackUnit(unit):
     def __init__(self, name, hp, damage):
         unit.__init__(self,name,hp)
         self.damage=damage  

     def attack(self,locattion):
         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
             .format(self.name, locattion, self.damage))  
             #self는 자기자신을 의미, self.name을 통해 자기 자신의 변수에 접근 할 수 있음
             #self를 적지 않으면 전달 받은 값을 쓴다는 의미
    
     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp-=damage
         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
         if self.hp<=0:
             print("{0} : 파괴되었습니다.".format(self.name))

#공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage,flying_speed):
        Flyable. __init__(self, flying_speed)
        AttackUnit. __init__(self, name, hp, damage)

Valkyrie=FlyableAttackUnit("발키리", 200, 6, 5)
Valkyrie.attack("5시")
Valkyrie.damaged(50)
Valkyrie.fly(Valkyrie.name, "3시")

#####-메소드 오버라이딩-#####

#일반 유닛
class unit:
    def __init__(self, name, hp, speed):
        self.name=name 
        self.hp=hp
        self.speed=speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]".format(self.name, location, self.speed))

#공격유닛       
class AttackUnit(unit):
     def __init__(self, name, hp, speed, damage):
         unit.__init__(self,name,hp,speed)
         self.damage=damage       

#공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        Flyable. __init__(self, flying_speed)
        AttackUnit. __init__(self, name, hp, 0, damage) #지상 speed 0

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)  

vulture=AttackUnit("벌쳐", 80, 10, 20)
battlecruiser=FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시") 
battlecruiser.fly(battlecruiser.name, "9시")
#vulture는 지상유닛, battlecruiser는 공중 유닛이기 때문에 각각 move함수 fly함수를 써야 함
vulture.move("11시") 
battlecruiser.move("9시")
#FlyableAttackUnit 클래스에 move 함수를 만들면 move함수로 통일할 수 있음

#####-pass-#####
class unit:
    def __init__(self, name, hp, speed):
        self.name=name 
        self.hp=hp
        self.speed=speed
 
#건물
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        pass #아무것도 안하고 일단은 넘어감

#서플라이 디폿: 건물, 1개 건물 = 8유닛    
supply_depot=BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#####-supper-#####
class unit:
    def __init__(self, name, hp, speed):
        self.name=name 
        self.hp=hp
        self.speed=speed
 
#건물
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        #unit.__init__(self, name, hp, 0)
        super().__init(name,hp,0) #super을 쓸 때는 ()를 붙이고 self를 빼고 씀
        #다중 상속을 할 때는 super을 사용하면 하나 밖에 상속이 되지 않기 때문에 사용X
        self.location=location

#Quiz 8
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

h1=House("강남","아파트","매매","10억","2010년")          
h2=House("마포","오피스텔","전세","5억","2007년") 
h3=House("송파","빌라","월세","2000년","500/50",) 

houses=[]
houses.append(h1)
houses.append(h2)
houses.append(h3)       

#####-예외처리-#####
#Try내부에 있는 문장을 실행하다가 문제가 발생했을 때 except부분에 해당하는 에러의 문장을 실행
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err) #에러 내용 출력
except Exception as err: #나머지 에러
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

#####-에러 발생시키기-#####
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError #의도적으로 에러를 발생시켜서 except로 내려오게 함
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

#####-사용자 정의 에러-#####
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요")     
    print(err)    
finally:
    print("계산기를 이용해주셔서 감사합니다") #에러가 발생하던지 말던지 무조건 실행    

#Quiz9

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")    
        elif order <= 0:
            raise ValueError    
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

#####-모듈-#####
#함수나 변수 또는 클래스를 모아 놓은 파일이다. 
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
##theater_module.py파일을 따로 만들어서 아래와 같은 3개의 함수 입력
# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다. ".format(people, people * 4000))

#################################################################################
import theater_module
theater_module.price(3) #3명이서 영화보러 갔을 때 가격
theater_module.price_morning(4) #4명이서 조조할인
theater_module.price_soldier(5) #5명의 군인이 영화 보러 갔을 때

import theater_module as mv #theater_module 대신 mv로 호출할 수 있음
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import*  #theater_module에 있는 것을 사용할 것임
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning #사용할 함수 지정
price(3)
price_morning(4)
# price_soldier(5) 쓸 수 없음

from theater_module import price_soldier as price
#price_soldier밖에 안쓰기 때문에 줄여서 price로 쓰도록 함
price(5)

#####-패키지-#####
#:모듈들을 모아놓은 집합 
#travel이라는 파일에 __init__.py, thailand.py, vietnam.py 생성하고 아래와 같은 코드 작성

#__init__.py
__all__=["vietnam"] # vietnam 모듈 공개

#thailand.py
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만")

if __name__ == "__main__": # 모듈 직접 실행
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else: # 외부에서 모듈 호출
    print("Thailand 외부에서 모듈 호출") 

 #vietnam.py   
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

###################################################################
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
trip_to = ThailandPackage() # travel.thailand. 는 생략
trip_to.detail()

from travel import vietnam # travel 패키지에서 vietnam 모듈 가져오기
trip_to = vietnam.VietnamPackage() # travel. 은 생략
trip_to.detail()

#어떤 대상을 import 하느냐에 따라서 대상 내에 접근하기 위한 코드도 달라져야 한다

from travel import *
trip_to = vietnam.VietnamPackage() # 베트남
trip_to.detail()

#* 을 쓴다는 것의 의미는 travel 이라는 패키지에 있는 모든 것을 가져다 쓰겠다는 것인데,
# 실제로는 패키지를 만든 사람이 공개 범위를 설정해줄 수가 있음 그걸 __init__에서 설정
# 해서 __init__에서 공개로 설정되어 있는 모듈만 사용 가능

