sw =[]
num = int(input('스위치 개수'))
if num<=100:
    for i in range(num):
        a = int(input('1과 0 사이의 숫자'))
        sw.append(a)
    student = int(input("100이하인 양의 정수이다"))
    for k in range(student):
        b,n = map(int,input('성별을 입력하여라 남학생은 1, 여학생은 2 학생이 받은 스위치 번호').split(' '))
        if b == 1 :
            for i in range(1,num):
                if n*i <= num:
                    if sw[n*i] == 1:
                        sw[n*i] = 0
                    else :
                        sw[n*i] = 1
                else:
                    continue
        elif b == 2 :
            if sw[n-1] == sw[n+1]:
                if sw[n-2] == sw[n+2]:
                    for k in range(num):
                        if sw[k] == 0:
                            sw[k] =1
                        else :
                            sw[k] = 0
for i in sw:
    print(i,end=' ')

