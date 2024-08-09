import datetime

day1 = datetime.date(2023,12,25)
print(day1)
week = day1.weekday()
match week :
    case 0:
        print('mon')
    case 1 :
        print('tue')
    case 2 :
        print('wed')
    case 3:
        print('thu')
    case 4 :
        print('fri')
    case 5:
        print('sat')
    case 6:
        print('sun')


import datetime
day2 = datetime.date(2024,1,1)
print(day2,day2.weekday())
week2 = day2.weekday()
if week2%2 == 0:
    print("짝수")
else :
    print("홀수")

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

"""
for _ in range(3):
    a = time.time()
    for i in range(10):
        print('%d초'%i)
    b = time.time()
    if b-a>=0.00001:
        print('10초간 쉬겠습니다. ')
        time.sleep(10)
    print('리셋합니다.')
print('종료합니다.')
"""
def find_day():
    year,month,day = map(int,input('찾고 싶으신 요일의 년도,날짜,일을 입력하시오').split(','))
    days = datetime.date(year,month,day)
    weeks = days.weekday()
    match weeks :
        case 0:
            print(year,month,day,'mon')
        case 1 :
            print(year,month,day,'tue')
        case 2 :
            print(year,month,day,'wed')
        case 3:
            print(year,month,day,'thu')
        case 4 :
            print(year,month,day,'fri')
        case 5:
            print(year,month,day,'sat')
        case 6:
            print(year,month,day,'sun')

def today_day():
    print(time.ctime())

while True:
    print("1.요일 찾기\n2.오늘 날짜\n3.종료")
    num = int(input())
    if num == 3:
        print("종료합니다")
        break
    elif num==1:
        find_day()
    elif num == 2:
        today_day()
    else :
        print("숫자를 잘못 입력하셨습니다.")
        continue

print(time.localtime(time.time()))
print(time.time())
print(time.asctime(time.localtime(time.time())))
