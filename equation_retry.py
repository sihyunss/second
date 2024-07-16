#사용자로부터 방정식을 받는다.
#2**(1/2) 루트 사용하는 방법 or print(math.sqrt(a))
import sys
import math

# return: 2차방정식의 항을 구하기 위해 만든 함수 입니다.
# eq:사용자로 부터 받음 값

def check_equal(eq): #eq에 = 이것이 존재하는 지 판단
    if '=' not in eq:
        print('=이 없으므로 종료합니다')
        sys.exit(1)

def check_degree(eq):
    if '^2' not in eq:
        print("이 방정식은 2차 방정식이 아닙니다.")
        sys.exit(1)

def order(first_num, finish_num, eq):#시작할 숫자를 줌으로써 상수를 찾는 과정 , if 을 써서 내 가 받은 문자에 - 가 있으면 -를 제외 하여 숫자를 만들엉라
    while True :
        if eq[finish_num] =='x':
            break
        if eq[finish_num] == '=':
            break
        finish_num+=1
    
    if finish_num == first_num: #함수로 묶자
        a = '1'
    elif finish_num - first_num == 1 and (equation[first_num:finish_num]=='+' or equation[first_num:finish_num] == '-') :
        if equation[first_num:finish_num] == '+':
            a = '1'
        else :
            a = '-1'
    else :
        a = equation[first_num:finish_num]
    return a,finish_num

#근의 방정식을 이용하여 x값을 구하는 것임
def result_root(a,b,c):
    denominator = 2*a
    molecule = -b+math.sqrt(b**2-4*a*c)
    x = molecule//denominator
    return x

equation = input('방정식을 입력하시오 (띄어쓰기 하지 않고 작성함)')

check_equal(equation)
check_degree(equation)

a,finish = order(0, 0, equation)
b,finish = order(finish+3, finish+3, equation)
c,finsih = order(finish+1, finish+1, equation)

if a == 0:
    print("2차 방정식의 값을 구할 수 없습니다.")
    sys.exit(-1)

print("2차 방정식의 해는 :",result_root(int(a),int(b),int(c)))


