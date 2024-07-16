"""str = input()

if str[0]<'0' or str[0]>'9':
    print('error')
    sys.exit(1)

stack = []
for i in range(0, len(str), 2):
    stack.append(str[i])

print(stack)"""

""""str = "kim si hyun is studying python"
n = 'i'
a = 0
while True:
    a = str.find(n, a)
    if a == -1:
        break
    print(a)
    a += 1"""

"""post_stack = input('방정식을 입력하시오 (띄어쓰기 하지마셈): ')
location_mul = []
location_div = []
location_add = []
location_sub = []

def find_location(n):
    location = 0
    while True:
        location = post_stack.find(n, location)
        if location == -1:
            break
        if n == '*':
            location_mul.append(location)
        elif n == '/':
            location_div.append(location)
        elif n == '+':
            location_add.append(location)
        elif n == '-':
            location_sub.append(location)
        location += 1

# 각 연산자에 대해 위치를 찾는 함수 호출
find_location('*')
find_location('/')
find_location('+')
find_location('-')

# 결과 출력
print("'*' 위치:", location_mul)
print("'/' 위치:", location_div)
print("'+' 위치:", location_add)
print("'-' 위치:", location_sub)
"""
"""a = []
b = a.pop(0)
if b == None:
    print('error')
"""

a = []
try:
    b = a.pop(0)
except IndexError:
    print('error: list is empty')
else:
    if b is None:
        print('error: value is None')

"""a = []
b = [1]
try :
    c = a.pop(0)
    d = b.pop(0)
except IndexError:
    if c is None :
        print('a가 값이 없습니다')
    elif d is Nonde:
        print('b가 없습니다')"""

a = []
b = []

try:
    c = a.pop(0)
except IndexError:
    print('a가 값이 없습니다')
    c = 1024  # 초기화

try:
    d = b.pop(0)
except IndexError:
    print('b가 값이 없습니다')
    d = 1024  # 초기화

# 추가 확인
if c == 1024 and d == 1024:
    print('둘다 존재 하지 않습니다.')

c = 1024
d = 10
if c > d :
    print('ㅐ긱')