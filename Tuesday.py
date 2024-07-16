s1 = set([1,2,3])
print(s1)#list로 출력됌
s2 = set("Hello")
print(s2)#중복을 허용하지 않는다. , 순서가 없다
l1 = list(s1) #리스트로 변환
sum = 0
for i in l1:
    print(i)
    sum += i#초기화 해줘야함
print("sum의 평균은 ",sum//3)
print("sum을 나머지 있는걸로 만드려면 ",sum/3)
s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s1&s2)#교집합
print(s3&s4)
print(s3 | s4) #중복되는 값이 안나옴!!!! 
print(s3.union(s4))#메소드드드드드드드
print(s4.intersection(s3))#교집합 메소드
print(s4-s3)#차집합
print(s4.difference(s3))#차집합 메소드
s4.add(10)#값을 추가할 수 있음~~
print(s4)
#print(s4.sub(10)) error!!
s4.remove(10)#값을 지울떄
print(s4)
s2 = set("kim si hyun")
print(s2) 
s2.update("test test test")#값을 업데이트 할때
print(s2)
#빈것을 돌려주면 거짓으로 나옴!!
a = [1,2,3,4]
while a:
    print(a.pop())#값을 꺼낼떄 사용하는 것
if []:
    print("true")
else :
    print("false")
if [1,2,3,4,5,6]:
    print("true")
else :
    print("false")
print(bool('true'))
print(bool('false'))#true 출력함
a = 1
b = "python"
c = [1,2,3]
print(id(a))#주소값을 알때
a = c
print(a)
print(a.pop())
print(a)
if a is c :
    print("same")
    print(c)#값 복사!!! 미친... 
else :
    print("diff")
print("c id = ",id(c))
print ("a id = ",id(a))#주소가 같네,, 108쪽까지 한거임

a = "true" if 10>20 else "flase"
print(a)
