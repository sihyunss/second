#토요일 1시간정도 공부함
#생년월일을 받아 출력하는 함수
#a = input("생년월일을 입력하시오")
#b = a.split()
#for i in range(3):
#    print(b[i])
"""
a = int(input("생년월일을 입력하시오"))
b[3] = a.split() 오류나는 이유는 c언어가 아니기때문에 또,
for i in range(3):
    print(i)
"""
#2003 06 
"""
a= input("생년월일을 입력하시오 ")
b[3] = a.split(' ')
for i in b:
    print(i)
a = int(input("생년월일을 입력하시오"))#int형으로 바꾸고 싶을 때 string형이 아니라
"""

#b = a.split()
#for i in range(3):
#    print(b[i])

#int형을 리스트에 값을 저장하고 출력하는 프로그램
""""
result = 0
for i in range(3):
    a = int(input("값을 입력하시오"))
for i in a:
    result += i;
print("합의 결과는",result)
오류오류오류오류오류오류오류오류오류오로유로유롱류오롱류
"""
# 해결을 해보자...
#sum = 0
#value = []
#a = int(input("더할 횟수를 입력하시오"))
#print("값을 입력하시오")
#for i in range(a):
#    b = int(input())
#    value.append(b)
#for i in range(a):
#    sum += value[i]
#print("다 더한 값은 ",sum)
"""
head = "Python "
tail = "fuckfuckfuckfuckfuㅎㅎㅎ"
print(head+tail)
a = "김시현 "
print(a*2)
print(len(a)) #a.len()이 아님 제발..
a = "Python is bad, I like C language"
print(len(a))
print(a[2])
print(a[:5])
print(a[-1])
print(a)
#현재온도를 츨정하여 만약 지금 온도가 20도면 값이 출력하고 종료하는
i = 0
while(True):
    i+=1
    if(i == 18 and i == 20):
        
        print("현재 온도는 %d입니다",i)
        break

"""