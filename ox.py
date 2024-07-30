#오목을 만들예정, 사용자는 입력받아서 0로 처리 , 컴퓨터는 질이 좀 떠러지지만 랜덤으로 해서 x으로 만약에 ,컴퓨터가 빠르면 컴퓨터에게 우선순위넘김 

"""
return :
선정할 위치를 입력하시오(ex: 3,3)1,1
o - -
- - -
- x -
선정할 위치를 입력하시오(ex: 3,3)2,2
o - -
- o x
- x -
선정할 위치를 입력하시오(ex: 3,3)3,3
사용자가 승리하였습니다.
o - -
- o x
- x o
"""

#컴퓨터가 알을 나야하기 때문에 랜덤함수를 사용함
import random


#사용자와 컴퓨터가 놨던 위치에 또 다시 놓을 수도 있기에 만든 함수
def corret_number (a,b):
    return omok[a][b]!='-'

#컴퓨터가 오목을 둘 수 있도록 만든 함수
def computer_put_on_omok():
    while True:
        a= random.randrange(0,3)
        b=random.randrange(0,3)
        if corret_number(a,b):
            continue
        else :
            break
    return a,b
    
#사람이 오목을 둘수 있도록 만든 함수
def person_put_on_omok():
    a,b = map(int,input('선정할 위치를 입력하시오(ex: 3,3)').split(','))
    a -=1
    b -=1
    return a,b

#지금 현재 컴퓨터와 사용자가 어디에 값을 놓았는지 보여주기 위한 판
def draw():
    for i in range(3):
        for j in range(3):
            print(omok[i][j] ,end=' ')
        print()

#정해진 횟수를 넘어서까지 승자가 나지 않을 경우를 대비하여 만든 함수
def init_omok():
    return [['-' for _ in range(3)] for _ in range(3)]

#종료 조건을 주어서 누가 이기는 지 판단하는 함수
def finish_condination(num,winner):
    for i in range(0,3):
        if omok[i][0] == omok[i][1] == omok[i][2]==num:
            print(winner+' 승리하였습니다')
            return True
        
        elif omok[0][i] == omok[1][i] ==omok[2][i]==num:
            print(winner+' 승리하였습니다')
            return True
        
        elif omok[0][0] == omok[1][1] == omok[2][2]==num:
            print(winner+' 승리하였습니다')
            return True
        
        elif omok[0][2] == omok[1][1] == omok[2][1]==num:
            print(winner+' 승리하였습니다')
            return True
            

omok = [['-' for _ in range(3)] for _ in range(3)]
n = 0 #정해진 횟수

while True:

    n+=1

    if n == 9:
        print('승부가 나지 않을 거 같습니다. 오목을 초기화합니다.')
        omok =init_omok()
    
    #사람에게 값을 받기
    person_a,person_b = person_put_on_omok()

    if corret_number(person_a,person_b):
        print('사용자가 잘못 입력하였습니다. 다시 입력하여 주세요')
        continue

    omok[person_a][person_b] = 'o'
    if finish_condination('o','사용자가'):
        draw()
        break
    computer_a,computer_b = computer_put_on_omok()

    omok[computer_a][computer_b]='x'
    if finish_condination('x','컴퓨터가'):
        draw()
        break
    draw()
    
