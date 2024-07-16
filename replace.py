import sys

def samex(a):
    for i in a:
        if i == '=':
            return False
    return True

def finds(a):
    for index, value in enumerate(a):
        if value == '^':
            return index
    sys.exit()

def pop(eq):
    return eq.pop(0)

def push(eq, n):
    eq.insert(0, n)

def s(eq, i, n):
    if n == 'x':
        if eq[0] == '^':
            pop(eq)
            b = pop(eq)
            if b == '2':
                push(eq, i ** 2)
            else:
                push(eq, i)
        else:
            push(eq, i)
    else:
        pass

def sum(eq, n):
    if n == '+':
        result = int(eq[0]) + int(eq[1])
        eq = eq[2:]
        push(eq, result)
    elif n == '-':
        result = int(eq[0]) - int(eq[1])
        eq = eq[2:]
        push(eq, result)
    elif n == '*':
        result = int(eq[0]) * int(eq[1])
        eq = eq[2:]
        push(eq, result)
    elif n == '/':
        result = int(eq[0]) // int(eq[1])
        eq = eq[2:]
        push(eq, result)
    elif n == '=':
        if int(eq[0]) == int(eq[1]):
            print(num)
            return False
        else:
            return True

def cam(eq):
    while eq:
        n = pop(eq)
        if n.isdigit() or (n.startswith('-') and n[1:].isdigit()):
            continue
        s(eq, num, n)
        if not sum(eq, n):
            break

num = -100
eq = list(input('방정식 (한칸 띄고 씀): ').split(' '))

if samex(eq):
    print('조건 1을 만족하지 않아 종료합니다.')
    sys.exit()

n = finds(eq)
if int(eq[n + 1]) > 2:
    print('조건 2에 맞지 않습니다.')
    sys.exit()

cam(eq)
