#삼각형의 넓이 및 사각형의 넓이 구하는 프로그램을 만들 예정
class Area_Rt:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Rectangle(self):
        return a*b
    def Squre(self):
        return a*a


class Area_Tr(Area_Rt):
    def Triangle(self):
        return (a*b)/2

def inputs():
    a,b = map(int,input('변을 입력하시오 ').split(','))
    return a,b

print("1. 직사각형의 넓이 \n2.정사각형의 넓이 \n3.삼각형의 넓이 \n원하는 번호를 누르시오")

num = int(input())

if num == 1 :
    a,b= inputs()
    q = Area_Tr(a,b)
    sum = q.Rectangle()
    print('직사각형의 넓이는 %d 입니다 .'%sum )    

elif num == 2 :
    a = int(input('면을 입력하시오 '))
    q = Area_Tr(a,0)
    print('정사각형의 넓이는 %d 입니다 .' %q.Squre()) 

else :
    a,b = inputs()
    q = Area_Tr(a,b)
    print('삼각형의 넓이는 %d 입니다 .' %q.Triangle()) 

#상속 할땐 self입력하시오
class AVG:
    result = 0
    def rectangle(self,a,b):
        result = a*b
        print('직사각형의 넓이는 %d 입니다. '%result)

    def squre(self,a):
        result = a*a
        print('정사각형의 넓이는 %d '%result)

class AVG2(AVG):
    def triangle(self,a,h):
        result = (a*h)//2
        print('삼각형의 넓이는 %d'%result)

print("1. 직사각형의 넓이 \n2.정사각형의 넓이 \n3.삼각형의 넓이 \n원하는 번호를 누르시오")

nums = int(input())

rc=AVG2()


match nums:
    case 1:
        a,b = map(int,input('변을 입력하시오 ').split(','))
        rc.rectangle(a,b)
    case 2:
        a = int(input('값을 입력하시오'))
        rc.squre(a)
    case 3:
        a,b = map(int,input('높이와 밑변을 입력하시오 ').split(','))
        rc.triangle(a,b)
        