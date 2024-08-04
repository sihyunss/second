#데이터 구조에서 공부했던 방정식을 이용하여 사용자로 부터 받은 함수를 출력한 후, 함수끼리 더하는 프로그램 코드를 짤 예정
""" return : 
최대 차수를 입력하시오 5 
차수의 앞 숫자들을 입력하시오
1
2
3
4
5
6
최대 차수를 입력하시오 3
차수의 앞 숫자들을 입력하시오
1
2
3
4
1번째 방정식 :  1x^5 + 2x^4 + 3x^3 + 4x^2 + 5x^1 + 6 = 0
2번째 방정식 :  1x^3 + 2x^2 + 3x^1 + 4 = 0
더한 결과의 방정식 :  1x^5 + 2x^4 + 4x^3 + 6x^2 + 8x^1 + 10 = 0"""


#사용자로부터 방정식을 받음
def input_degree ():
    degree = int(input("최대 차수를 입력하시오 "))
    coef = []
    print('차수의 앞 숫자들을 입력하시오')
    for i in range(0,degree+1):
        a = int(input())
        coef.append(a)
    return coef,degree


#사용자로 부터 받은 방정식을 알려주고, 두개의 함수를 더한 방정식을 출력해주는 함수
def print_degree(commit,coef,degree):
    num = degree 
    print(commit,end=" ") #몇번째 언어인지 표시하기 위한 print
    for i in coef:
        print("%dx^%d +"%(i,degree),end=' ')
        degree-=1
        if degree == 0:
            break
    print("%d = 0"%(coef[num]))

#2개 함수를 더하는 함수임, 그러기 위해서는 첫번째 차수가 더 큰지 두번쨰 차수가 더 큰지 비교하여 더하는 함수임
def add_equation(coef1,degree1,coef2,degree2):
    
    if degree1 > degree2 :
        for i in range(0,degree2+1):
            coef1[i+(degree1-degree2)] += coef2[i]
        return coef1,degree1
    elif degree2 > degree1:
        for i in range(0,degree1+1):
            coef2[i+(degree2-degree1)] += coef1[i]
        return coef2,degree2
    else :
        for i in range(0,degree1+1):
            coef1[i]+=coef2[i]
        return coef1,degree1      


coef1,degree1 = input_degree()
coef2,degree2 = input_degree()

add_stack = []

print_degree("1번째 방정식 : ",coef1,degree1) #계산 하기 전에 출력하기 위함

add_stack,add_degree=add_equation(coef1,degree1,coef2,degree2)

print_degree("2번째 방정식 : ",coef2,degree2)
print_degree("더한 결과의 방정식 : ",add_stack,add_degree)