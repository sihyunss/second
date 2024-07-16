#일요일 공부 내용
number = 3
print("I eat %s apples"%number)
print("I eat %s appeles ",number)#이렇게 치면 안돼ㅐㅐㅐㅐㅐㅐㅐㅠ
number = 10
day = "three"
print("숫자 %d 영어로는 %s "%(number,day))
print("숫자 {0} 영어로는 {1}".format(number,day))
print("숫자 {a} 영어로는 {b}".format(a=10,b= "ten"))
print("숫자 %d "%(3))
print("숫자 {n}".format(n = "kim"))
print("숫자 {1}".format(1,2))
print("숫자는 {}    {}".format(1,2))
print("숫자는 바보 {2} {1}".format("kim","si","hyun"))
"""
a = int(input())//입력 받는 값
b = int(input())//입력 받는 값
for i in range(a): //횟수에 맞게 반복됌
    for j in range(b)://위랑 똑같음
        print("i는",i,"j는",j) //값들을 출력함

def get_input_until_zero()://함수
    num_list = []//리스트 초기화
    while True://무한 루프
        num = int(input("숫자를 입력하세요. 종료하려면 0을 입력하세요: "))
        if num == 0:
            break//0을 집어 넣으면 멈추게 하기 위하여
        num_list.append(num)//list에 값을 추가해주는 
    
    if len(num_list)==0://길이
        print("입력 받은 값이 없습니다.")//없으면 오류라는 메세지
    else://아니면 최솟값을 구하는지 최대값을 구하는 지 함수를 이용하여 구함
        print(f"최대값: {max(num_list)}, 최소값: {min(num_list)}")

get_input_until_zero()//함수 호출~~~~~
"""
a = "kim si hyun"
print(len(a))
print(a.count('i'))
print(a.find('h'))
print(",".join(['a','b','c']))
