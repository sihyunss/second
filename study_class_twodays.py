class Animal:
    legs = 4
    def talk(self):
        print("Animals can't talk")
a = Animal()
print(a.legs)

class Dog(Animal):
    def talk(self):
        print("멍멍멍멍멍")

class Cat(Animal):
    def talk(self):
        print("야옹")

class Snake:
    legs = 0
dog = Dog()
dog.talk()
cat = Cat()
cat.talk()
a.talk()
snake = Snake()
print(snake.legs)
#파이썬은 오버로딩 안된다, 가변인자를 쓰자
"""
class Sum:
    def avg(a):
        return a*a
    def avg(c,b):
        return c*b

s = Sum()
print(s.avg(10))
print(s.avg(10,20))
"""

class Sum:
    def avg(self,*a):
        if len(a) == 1:
            print("정사각형의 넓이는",a[0]*a[0])
        else :
            print("직사각형의 넓이",a[1]*a[0])
s = Sum()
s.avg(10)
s.avg(10,20)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        result = self.x + self.y
        return result
    def sub(self):
        result = self.x - self.y
        return result
point = Point(10,10)
print(point.add())
print(point.sub())

class Points(Point):
    def mul(self):
        result = self.x*self.y
        return result
    def div(self):
        result = self.x/self.y
        return result
points = Points(10,2)
print(points.mul())
print(points.div())

class WhileTrue:
    def __init__(self,result):
        self.result = result
    def add(self,x):
        self.result += x
        return self.result
    def sub(self,y):
        self.result-=y
        return self.result
    def print_result(self):
        print("result = ",self.result)

w = WhileTrue(0)
w.print_result()
print("add",w.add(10))
print("sub",w.sub(4))

w1 = WhileTrue(10)
w1.print_result()
print("add", w1.add(5))
print("sub",w1.sub(5))
