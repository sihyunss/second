post_stack = input('방정식을 입력하시오 (띄어쓰기 하지마셈): ')
copy_post_stack=[]
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
i = 0#인덱스 값을 같게 하기 위한
def postfix_statck(n):
    first = post_stack[n-1]
    op = post_stack[n]
    second = post_stack[n+1]
    copy_post_stack.insert(first)
    copy_post_stack.insert(second)
    copy_post_stack.insert(op)


while True:
    """if not location_mul[0] or location_div[0]:
            if not location_mul[0] and location_div[0]:
                break
            elif not location_mul[0]:
                postfix_statck(location_div[0])
            elif not location_div[0]:
                post_stack(location_mul[0])
    if location_mul[i] < location_div[i]:
        #pop으로 생각을 해보자고 !! 
        postfix_stack(location_mul[i])
    elif location_mul[i] > location_div[i]:
        postfix_stack(location_div[i])"""
    try :
        mul = location_mul.pop(0)
    except IndexError:
        mul = 1024
    try :
        div = location_div.pop(0)
    except IndexError:
        div = 1024
    if div == 1024 and mul == 1024 : #오류 숫자
        break
    
    if mul<div :
        post_stack(mul)
        location_div.insert(div,0)
    elif mul>div :
        post_stack(div)
        location_mul.insert(mul,0)
    


