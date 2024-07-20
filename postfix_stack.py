#사용자에게 받은 수식을 후위 수식으로 표기해주고, 후위수식으로 값을 내림

"""
return :
수식을 입력하시오 (중위표기식 : a + b * c (띄어쓰기 해주세요))10 * 2 / 5 + 4
후위수식 : 10 2 * 5 / 4 +
계산 값은  8
"""

inorder_stack = list(input('수식을 입력하시오 (중위표기식 : a + b * c (띄어쓰기 해주세요))').split(' '))

postfix_stack = [] #후위수식으로 만들 리스트
operator_stack = [] #연산자를 저장할 리스트
sum_stack = [] #후위수식을 저장할 리스트

def inorder_pop():
    return inorder_stack.pop(0)

def operator_pop():
    return operator_stack.pop()

def postfix_pop():
    return postfix_stack.pop(0)

def sum_pop():
    return sum_stack.pop()

def operator_push(coef):
    operator_stack.append(coef)

def postfix_push(coef):
    postfix_stack.append(coef)

def sum_push(coef):
    sum_stack.append(coef)

#연산자의 스택에서 값을 꺼내 우선순위를 가리는 함수
def priority_operator(op):
    match op:
        case '*':
            return 1
        case '/':
            return 1
        case '+':
            return 2
        case '-':
            return 2
        case '(':
            return 0
        case ')':
            return 0
        
#후위수식을 만드는 과정(중위리스트에서 값을 꺼냄, 꺼낸값이 연산자면, 연산자 스택에 다른 연산자 있는지 확인후, 우선순위 파악 후 후위로 값을 뺄지 아니면 연산자 리스트에 넣을지 판단하는 과정)
for _ in range(0,len(inorder_stack)):
    a = inorder_pop()
    if a == '+' or a == '*' or a =='/' or a=='-':
        if '+' in operator_stack or '-' in operator_stack or '/' in operator_stack or '*' in operator_stack:
            b = operator_stack[len(operator_stack)-1]
            numa=priority_operator(a)
            numb=priority_operator(b)
            
            if numb<=numa:
                b=operator_pop()
                postfix_push(b)
                operator_push(a)
            else :
                operator_push(a)
            
        else :
            operator_push(a)
    else :
        postfix_push(a)

#연산자리스트에 값을 다 빼서 출력함
for _ in range(0,len(operator_stack)):
    a = operator_pop()
    postfix_push(a)

#사용자에게 값을 출력하여 이런 후위수식이 만들어졌다는 것을 보여줌
print("후위수식 :",end = ' ')
for i in postfix_stack:
    print(i,end=' ')

#후위수식을 계산하는 과정, 후위리스트에서 값을 꺼내 꺼낸값이 숫자면 스택에 저장후, 피연산자가 나오면 스택에서 값을 꺼내서 int로 바꾼후 연산자에 맞게 계산후 다시 스택에 저장하는 과정을 함
for _ in range(0,len(postfix_stack)):
    op = postfix_pop()
    if op.isdigit():
        sum_push(op)
    else :
        second = int(sum_pop())
        first = int(sum_pop())
        if op == '+':
            sum_push(str(first+second))
        elif op == '-':
            sum_push(str(first-second))
        elif op == '/':
            sum_push(str(first//second))
        elif op == '*':
            sum_push(str(first*second))

print()
print("계산 값은 ",sum_pop())
