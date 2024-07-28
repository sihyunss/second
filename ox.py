#오목을 만들예정, 사용자는 입력받아서 0로 처리 , 컴퓨터는 질이 좀 떠러지지만 랜덤으로 해서 x으로 만약에 ,컴퓨터가 빠르면 컴퓨터에게 우선순위넘김 

import random



def corret_number (a,b):
    return omok[a][b]!='-'

def computer_put_on_omok():
    while True:
        a= random.randrange(0,3)
        b=random.randrange(0,3)
        if corret_number(a,b):
            continue
        else :
            break
    return a,b
    

def person_put_on_omok():
    a,b = map(int,input('선정할 위치를 입력하시오(ex: 3,3)').split(','))
    a -=1
    b -=1
    return a,b

def draw():
    for i in range(3):
        for j in range(3):
            print(omok[i][j] ,end=' ')
        print()

def init_omok():
    return [['-' for _ in range(3)] for _ in range(3)]

omok = [['-' for _ in range(3)] for _ in range(3)]
n = 0
while True:
    n+=1
    if n == 4:
        print('승부가 나지 않을 거 같습니다. 오목을 초기화합니다.')
        omok =init_omok()
    
    person_a,person_b = person_put_on_omok()
    if corret_number(person_a,person_b):
        print('사용자가 잘못 입력하였습니다. 다시 입력하여 주세요')
        continue

    omok[person_a][person_b] = 'o'

    computer_a,computer_b = computer_put_on_omok()

    omok[computer_a][computer_b]='x'
    
    draw()
    
