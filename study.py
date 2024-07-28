"""a = 'x^2+x-2=0'
if 'x^2' in a:
    print('ok')
a = 'x^2+x-2=0'
if 'x^2' not in a:
    print('이 방정식은 2차 방정식이 아닙니다.')
else:
    print('이 방정식은 2차 방정식입니다.')
a = '6x^2'
index=a.find('x^2')
if '0'<=a[0:index]<='100':
    print(a.find('0'<=a[0:index]<='100'))
if 'x^2' in a[0:3]:
    print('ok')
else : 
    print('숫자 있음')

if '0'<=a[0]<='1000':
    print(a[0])
else :
    print('오류')
if a[0] == '-':
    print('-')
else :
    print('+')

dict = '10x^2+x-2=0'
if '0'<=a[0]<='1000':
    b = a[0:5]
    print(b-'x^2')
num = 1

while True:
    if dict[num] == 'x':
        if dict[0] =='x':
            a = 1
        int(a)
        break
    a= dict[num]
    num +=1
print(a)

while True :
    if dict[num] =='x':
        break
    num+=1
print(int(dict[0:num]))
print(int(-10)+10)

op = [1,2,3,4,5,6,7,8,9,10]
print(op[len(op)-1])
inorder_stack = list(input('수식을 입력하시오 (중위표기식 : a + b * c (띄어쓰기 해주세요))').split(' '))
postfix_stack = []
operator_stack = []

def inorder_pop():
    return inorder_stack.pop(0)

def operator_pop():
    return operator_stack.pop()

def operator_push(coef):
    operator_stack.append(coef)

def postfix_push(coef):
    postfix_stack.append(coef)

def priority_operator(op):
    # 연산자의 우선 순위를 반환하는 함수
    if op == '*' or op == '/':
        return 1
    elif op == '+' or op == '-':
        return 2
    elif op == '(' or op == ')':
        return 0
    else:
        return -1  # 그 외의 경우, 예를 들어 피연산자

# 입력된 중위 표기식을 후위 표기식으로 변환하는 코드
for _ in range(len(inorder_stack)):
    a = inorder_pop()
    
    if a in '+-*/':
        while operator_stack and priority_operator(operator_stack[-1]) >= priority_operator(a):
            b = operator_pop()
            postfix_push(b)
        operator_push(a)
    elif a == '(':
        operator_push(a)
    elif a == ')':
        while operator_stack and operator_stack[-1] != '(':
            b = operator_pop()
            postfix_push(b)
        operator_pop()  # '(' 제거
    else:
        postfix_push(a)

# 남아 있는 모든 연산자를 후위 표기식 스택에 추가
while operator_stack:
    b = operator_pop()
    postfix_push(b)

# 후위 표기식 출력
print("후위표기식:", ' '.join(postfix_stack))

a = []
if '*'or '/' or'+' in a:
    b = a[len(a)-1]
    print(b)


inorder_stack = list(input('수식을 입력하시오 (중위표기식 : a + b * c (띄어쓰기 해주세요)): ').split(' '))

postfix_stack = []
operator_stack = []

def inorder_pop():
    return inorder_stack.pop(0)

def operator_pop():
    return operator_stack.pop()

def operator_push(coef):
    operator_stack.append(coef)

def postfix_push(coef):
    postfix_stack.append(coef)

def priority_operator(op):
    match op:
        case '*':
            return 2
        case '/':
            return 2
        case '+':
            return 1
        case '-':
            return 1
        case '(':
            return 0
        case ')':
            return 0

def process_operator(a):
    while operator_stack and priority_operator(operator_stack[-1]) >= priority_operator(a):
        postfix_push(operator_pop())
    operator_push(a)

for _ in range(len(inorder_stack)):
    a = inorder_pop()
    if a in ['+', '*', '/', '-']:
        process_operator(a)
    elif a == '(':
        operator_push(a)
    elif a == ')':
        while operator_stack and operator_stack[-1] != '(':
            postfix_push(operator_pop())
        operator_pop()  # Pop the '(' from the stack
    else:
        postfix_push(a)

while operator_stack:
    postfix_push(operator_pop())

print(' '.join(postfix_stack))


def priority_operator(op):
    if op in ('*', '/'):
        return 1
    if op in ('+', '-'):
        return 2
    return 0

def inorder_to_postfix(inorder_stack):
    postfix_stack = []
    operator_stack = []
    
    for a in inorder_stack:
        if a.isdigit():
            postfix_stack.append(a)
        elif a in ('+', '-', '*', '/'):
            while (operator_stack and
                   priority_operator(operator_stack[-1]) <= priority_operator(a)):
                postfix_stack.append(operator_stack.pop())
            operator_stack.append(a)
        elif a == '(':
            operator_stack.append(a)
        elif a == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_stack.append(operator_stack.pop())
            operator_stack.pop()  # pop '('

    while operator_stack:
        postfix_stack.append(operator_stack.pop())
    
    return postfix_stack

def evaluate_postfix(postfix_stack):
    sum_stack = []
    
    for a in postfix_stack:
        if a.isdigit():
            sum_stack.append(int(a))
        else:
            b = sum_stack.pop()
            c = sum_stack.pop()
            if a == '+':
                sum_stack.append(c + b)
            elif a == '-':
                sum_stack.append(c - b)
            elif a == '*':
                sum_stack.append(c * b)
            elif a == '/':
                sum_stack.append(c / b)
    
    return sum_stack[0]

# Input and process
inorder_stack = list(input('수식을 입력하시오 (중위표기식 : a + b * c (띄어쓰기 해주세요))').split())

postfix_stack = inorder_to_postfix(inorder_stack)
print('Postfix Expression:', ' '.join(postfix_stack))

result = evaluate_postfix(postfix_stack)
print('Evaluation Result:', result)
"""

a = ['1','2','+']
if '1000' in a:
    print(0)
a = ['+','1']
b  = str(a)
b = a.pop()
print(b)
"""if b.isdigit():
    print('ok')
    print(type(b))

print(b)
for i in a :
    b =i 
print(b)"""
"""a = int(a)
print(type(a))"""

