#데이터 구조에서 공부했던 방정식을 이용하여 사용자로 부터 받은 함수를 출력한 후, 함수끼리 더하는 프로그램 코드를 짤 예정

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
def print_degree(coef,degree):
    num = degree 
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
add_stack,add_degree=add_equation(coef1,degree1,coef2,degree2)
print_degree(add_stack,add_degree)