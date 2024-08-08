#연월일수로 나와
#https://wikidocs.net/33
import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)
diff = day2 - day1
print(diff.days)
print(day1)
print(day2)

day = datetime.date(2021,12,14)
print(day.weekday())#월요일 화요일
print(day1.weekday())#월요일은 0 이고 ... 일요일은 6

print(day.isoweekday()) #월요일이 1 이고 ... 일요일은 7임

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

#time.asctime(time.localtime(time.time())) 이것을 간단하게 
print(time.ctime())
print(time.strftime('출력할 형식 포맷코드 %c',time.localtime(time.time())))

import time
print(time.strftime('%x',time.localtime(time.time())))

"""
import time
for i in range(10):
    print(i)
    time.sleep(1)

for i in range(10):
    print("%d초 "%i)
    time.sleep(0.5)
"""

print(time.localtime())
print(time.asctime())
print(time.strftime('%c'))

#최대공약수
import math
print(math.gcd(60,100,80))

#최소 공배수 
import math
print(math.lcm(15,25))

import random
print(random.random())#0.0-1.0
print(random.randint(1,10)) #정수중에 

def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

data= [1,2,3,4,5]
print(random.sample(data,len(data)))
print(random.sample(data,3))

students = ['김시현','김시온','김가현','문소원','김진규']
snacks = ['사탕','초콜릿','젤리']

result = zip(students,snacks)
print(list(result))
print(result) #주소가 나와

import itertools
students = ['김시현','김시온','김가현','문소원','김진규']
snacks = ['사탕','초콜릿','젤리']
result = itertools.zip_longest(students,snacks,fillvalue='새우깡')
print(list(result))

import itertools
""" #중복을 허용하지 않음
print(list(itertools.permutations(['1','2','3'],2)))

print(list(itertools.combinations(['1','2','3'],2)))

#로또 처럼 45개의 숫자중 6개를 선택하는 경의수
import itertools
it = itertools.combinations(range(1,46),6)
for num in it:
    print(num)
print(len(list(itertools.combinations(range(1,46),6))))
"""
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)

import functools

#reduce에 선언한 람다 함수를 data 요소에 처례대로 누적 적용하여 계산
data = [1,2,3,4,5]
result = functools.reduce(lambda x,y : x + y , data)
print(result)

#최댓값 구하기

num_list = [3,2,8,1,6,7]
max_num = functools.reduce(lambda x,y : x if x > y else y, num_list)
print(max_num)

from operator import itemgetter
students = [("kim",22,'A'),("bark",32,'B'),("sally",17,'B')]
result = sorted(students,key = itemgetter(1))
print(result)
result1 = sorted(students,key = itemgetter(0))
print(result1)
result2 = sorted(students,key = itemgetter(2))
print(result2)

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
result = sorted(students,key = itemgetter('age'))
print(result)
result1 = sorted(students,key = itemgetter('name'))
print(result1)
result2 = sorted(students,key=itemgetter('grade'))
print(result2)
from operator import attrgetter
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]
result = sorted(students,key=attrgetter('age'))
import pickle
f = open("test.txt",'wb')
data = {1:'python',2:'you nedd'}
pickle.dump(data,f)
f.close()
import os
print(os.environ)
print(os.environ['PATH'])

"""
import time
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s \n"%i)

print("Start")

for i in range(5):
    long_task()
print("End")


import time 
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s \n"%i)
print("Start ")

threads  = []

for i in range(5):
    t = threading.Thread(target = long_task)
    threads.append(t)

for t in threads:
    t.start()
print("END")

for t in threads:
    t.join()
print("End")
"""

import tempfile
filename = tempfile.mkstemp()
print(filename)

def a():
    return 1/0
def b():
    a()
def main():
    try:
        b()
    except:
        print("오류가 발생하였습니다")

main()

import traceback
def a():
    return 1/0
def b():
    a()
def main():
    try:
        b()
    except:
        print("오류가 발생하였습니다. ")
        print(traceback.format_exc())

main()

"""{
    "name": "홍길동",
    "birth": "0525",
    "age": 30
}

import json
with open('myinfo.json') as f:
    data = json.load(f)
print(type(data))
print(data)"""

import webbrowser
webbrowser.open_new('https://wikidocs.net/33')