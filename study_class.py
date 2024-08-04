class Hello:
    def greetings(self):
        print("hello")
a = Hello()
a.greetings()

class Adios:
    def greetings(self,a):
        name = a
        return name
b = Adios()
print(b.greetings("bye"))


class Calculation:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result+=num
        return self.result
cal1 = Calculation()#인스턴스
cal2 = Calculation()
cal1.add(10)#구체화
cal2.add(20)
print(cal2.add(20))

"""class C:
    def add(self,num):
        self.num += num
        return self.num
a=C()
print(a.add(10))
print(a.add(20))"""

class Calculate:
    result = 0
    def add(self,num):
        self.result+=num
        return num
    
ass = Calculate()
print(ass.add(10))
print(ass.add(20))#값이 변하지 않는다.

class Cal:
    def __init__(self,result):
        self.result = result
    def add(self,num):
        self.result += num
        return self.result
calc = Cal(0)
print(calc.add(10))
print(calc.add(20))

class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
a = FourCal(4,2)
print(a.add())

#상속
class MoreFourCal(FourCal):
    pass
a = MoreFourCal(4,2)
print(a.add())

class MF(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
a = MF(4,2)
print(a.pow())

class SaFeFourCal(FourCal):
    def div(self):
        if self.second ==0 :
            return 0
        else :
            return self.first /self.second

a = SaFeFourCal(4,0)
print(a.div())

class Name:
    lastname = "김"

a = Name()
print(a.lastname)
a.lastname = "김시현"
print(a.lastname)
b = Name()
print(b.lastname)

num = 1
match num:
    case 1:
        print('1')
    case 2:
        print('2')

    case 3:
        print('3')

match num:
    case 1:
        pass
    case 2:
        print('2')
        print('1')
    case 3:
        print('3')