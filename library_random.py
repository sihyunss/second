#복권을 만들어 볼생각임 

import random
import time

#사용자에게 4개의 번호를 받는 함수
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

#추첨하고, random함수가 확률을 계산하기 위해서 배열을 만들어 나온 수를 더하고, 몇개 담청됐는지 확인하는 함수
def check_lottery_number(user,ai):
    num = 0
    result_lottery_number = []
    for i in range(4):
        a = random.randint(1,10)
        result_lottery_number.append(a)
        ai[a-1]+=1
        if user[i] == a:
            num+=1
    print("번호는 ",end = ' ')
    for i in result_lottery_number:
        print(i,end = ' ')
    print('입니다')
    print(str(num)+"개 담청되었습니다")

    time.sleep(3)

#배열에 갯수가 가장 높은 수를 추천해주는 함수
def number_recommendation(ai):
    ai_copy = ai[:]
    recommend = []
    for _ in range(4):
        max_num = max(ai_copy)
        if max_num == 0 :
            break
        num = ai_copy.index(max_num)+1
        recommend.append(num)
        ai_copy[num-1] = 0
    print("추천번호 :",recommend)
    time.sleep(1)

user_lottery_numbers=[]
probability_lottery_number = [0]*10

while True:
    
    print("1.복권구매 \n2.복권 담청 현장 \n3.python이 복권 번호 추천\n4.종료")
    num = int(input())
    if num == 4:
        break
    if num == 1:
        user_lottery_numbers = buy_lottery()
        print(user_lottery_numbers)
    elif num == 2:
        check_lottery_number(user_lottery_numbers,probability_lottery_number)
    elif num == 3:
        number_recommendation(probability_lottery_number)
