"""
money = True
if money:
    print("택시를 타고 가라")
else :
    print("걸어가라")
a = int(input("값을 입력 받아라"))
if(a>11000):
    print("택시를 타고 가라")
    print("택시비는 10000")
    print(str(a-100000)+"남았습니다")
else :
    print("버스타고 가라")


a = input("카드가 있어?? (맞으면 1,아니면 0)")
if a == '1':
    print("택시타자")
money = card = 0
b = input("돈이나 카드가 있니??(있으면 1, 없으면 0)")
if(b == '1'):
    c = input("돈이 있으면 m 카드가 있으면 c")
    if c == 'm':
        money = int(input("돈 얼마 있어??"))
    else :
        card = int(input("카드에 얼마 있어??"))
else :
    print("걸어가 이자슥아")

if money >= 10000 or card >= 10000:
    print("택시타")
else :
    print("걸어가 이 자식아")

#and or not으로 작성해줘야함
#in 과 not in 연산자로 리스트 안에 값이 있는지 확인해 볼수 있따,
if 6 in [1,2,3,5,4]:
    print("원하는 숫자가 리스트 안에 있음")
elif 3 in [2,1,24,5,4,3]:
    print("우너하느느을ㄴ")
else :
    print("원하는 숫자를 찾을 수 없습니다")

pocket = ['paper','cellphone','tap','notebook']
for i in pocket:
    print(i)
    if "paper" == i:
        print("여기 있어어ㅓ어")
        break
if 'money' in pocket:
    print("여기 있어욜")
else :
    print("없음 딴데에서 찾아 시키야")


print('sfd' not in pocket) #결과는 true

while True:
    a = int(input("아무 값이나 입력하시오"))
    if a == 0:
        print("종료 합니다")
        break
    elif a %2 == 0:
        print("짝수내요??")
    else :
        pass

pocket = ['money','cellphone','paper']
if 'money' in pocket : pass #한줄로 쓸수 있다. pass 를 이용하여 
else :
    print("원하시는 값이 없습니다")
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

score = int(input("아무 값이나 입력하시오 "))
message = "성공" if score >= 60 else "실패"
print(message)

money = int(input("돈이 얼마 있어?? "))
a  = "택시 타고 갈 수 있습니다" if money >= 100000 else "타지 못하는 군"
print(a)"""
#"""" 문자열로 취급함
#이게 가능 함!!
promt = """
1. Add 
2. Del 
3. List 
4. Quit
Enter number : """

number = 0
while number != 4:
    print(promt)
    number = int(input())