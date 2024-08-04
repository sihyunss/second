class Animal:
    legs = 4
    def talk():
        print("Animals can't talk")
a = Animal()
print(a.legs)

class Dog(Animal):
    def talks():
        print("멍멍멍멍멍")
class Cat(Animal):
    def talk():
        print("야옹")

class Snake:
    legs = 0
dog = Dog()
dog.talks()

