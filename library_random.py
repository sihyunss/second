#복권을 만들어 볼생각임 

import random
import time

def buy_lottery():
    user_lottery_number = []
    while True:
        print("원하는 숫자4개의 자리를 입력하시오(10아래로)")
        for i in range(4):
            a = int(input())
            user_lottery_number.append(a)
        print('사용자가 입력하신 숫자는 %d , %d , %d ,%d 입니다.'%(user_lottery_number[0],user_lottery_number[1],user_lottery_number[2],user_lottery_number[3]))
        answer = input('이대로 접수 하시겠습니까 ? (y or n)')
        if answer == 'n':
            user_lottery_number=[]#초기화하기
            continue
        else :
            print('접수 완료되었습니다.')
            return user_lottery_number

def check_lottery_number(user):
    print(user)

user_lottery_numbers=[]

while True:
    
    print("1.복권구매 \n2.복권 담청 현장 \n3.python이 복권 번호 추천\n4.종료")
    num = int(input())
    if num == 4:
        break
    if num == 1:
        user_lottery_numbers = buy_lottery()
        print(user_lottery_numbers)
    elif num == 2:
        check_lottery_number(user_lottery_numbers)
