result = 0
def add(num):
    global result
    result += num
    return result
print(add(10))
print(add(10))

"""class Cal:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    cal = Cal()
    cal2 = Cal()
    print(cal.add(3))
    print(cal2.add(4))"""
class Sum:
    def __init__(self):
        self.result = 0
    def add (self,num):
        self.result += num
        return self.result
    def sub(self,num):
        self.result -=num
        return self.result
    def mul(self,num):
        self.result *= num
        return self.result
a = Sum()
b = Sum()
print(a.add(10))
print(b.sub(5))
print(a.sub(5))#객체 단위로

class set:
    def __init__(self,one,two):
        self.one = one 
        self.two = two
a = set(4,1)
print(a.one)

class F:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def set(self,first,second):
        self.first = first
        self.second= second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
a = F(10,2)
print(a.first)
print(a.add())
