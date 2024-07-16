import sys
global front
front = 0
global front1
front1 = 0
global num
num = -100
avg = []
#1차원 인지, 2 차원인지,
# 함수 이름을 살짝 바꿔보면 좋을 것 같아. 나는 함수 이름이 잘 이해 안되네.
def equals_find(eq): #리스트를 인자로 받음, 조건 1 을 만족하는지,,,,
    return '=' not in eq

# 무엇을 찾는 함수인지 함수 이름에 써놓으면 좋을 것 같아.
def order_find(a): #리스트안에 ^지수승을 뜻하는 바를 찾는 것이 목적인 함수
    n = 0
    for i in a:
        n += 1
        if i == '^':
            print(n)
            return n
    sys.exit()

# 파이썬 리스트는 .pop() 메서드가 있으니, 메서드를 사용하는게 좋을듯
def pop(arr,i):
    n=arr.pop(i) # 이 front 변수는 초기화가 안되어있어서 오류라네.
    return n


# 파이썬 리스트는 .append() 메서드가 있으니, 메서드를 사용하는게 좋을듯
def push(n):
    global front1
    avg.insert(front1,n) # 이 front 변수는 초기화가 안되어있어서 오류라네.
    front1 +=1

# 무엇을 하는 함수인지 함수 이름을 잘 지어주면 좋을듯.
def check_degree(eq,i,n):
        global front
        if n == 'x' :
            k = pop(eq,0)
            if k =='^':
                b = pop(eq,0)
                if b == '2':
                    #front =-1
                    push(i ** 2)
            else :
                #front -= 1
                push(i)
                push(k) #push 이상한 감지!! front1 ...
        elif n == '=':
            push(n)
            a = pop(eq,0)
            push(a)
            return True
        else :
            push(n)
num_degree = 0
# 파이썬에는 match-case 문이 있는데, switch-case랑 똑같으니까 써보면 좋을듯.
def sum(avg,n):
    global num
    global front1
    global num_degree
    first = 0
    if n >= -100 or n<=100:
        next = str(pop(avg,0))
        first=pop(avg,0)
        front1 = 0
    match next :
        case '+':
            push(int(n)+int(first))
        case '-':
            push(int(n)-int(first))
        case '*' :
            push(int(n)*int(first))
        case '/' :# 정수만 상대하기 위한
            push(int(n)/int(first))
        case '=':
            if int(first) == int(n):
                print(num)
                num_degree+= 1
                num+= 1
                if num_degree>2:
                    return True
            else : # 어차피 위에 if문에서 리턴을 하니까, 이 else문은 필요 없을듯
                num+= 1

# 뭐하는 함수인지 이해가 잘 안돼ㅠㅠ
def keep(eq):
    global num
    global front
    global front1
    for _ in range(len(eq)):
        n = pop(eq,0)
        if check_degree(eq,num,n):
            break
    
    #front = 0
    front1 = 0
    while True:
        n=pop(avg,0)
        if sum(avg,n) :
            break #만약 x값이 2가넘어가면 종료하는 조건이 있어야할 거같아 만든 if문
        if num>100 :
            break

# 이 부분이 c언어로 치면 main함수 부분이니까 각주를 달아주거나 main함수로 감싸주고
# 맨 밑에 main함수를 호출해주면 좋을듯?

def main():
    eq= list(input('방정식 (한칸 띄고 씀): ').split(' '))
    if equals_find(eq): # '=' 이것이 있는지 없는지에 대해 생각
        print('조건 1을 만족하지 않아 종료합니다.')
        sys.exit()
    n = order_find(eq)
    #지수승의 인덱스 값을 반환 받는다.
    if int(eq[n])  >2 :
        print('조건 2에 맞지 않습니다. ')
        sys.exit()
    keep(eq)

main()