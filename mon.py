#딕셔너리 추기,삭제
a = {1:'a'}
a[2] = 'b'
#print(a)
a[3] = 'c'
a[4] = 'd'#추가할때는 이걸로 사용 새로 만들떄는 a = {4:'d'}
a['kim'] = 'sihyun'
print(a)
#del a['kim']
del a[1]
print(a)
print(a[2])#요소 반환
print(a.keys())#키 값만 출력함
for i in a.keys():
    print(i)
for k in a.values():#키 값의 뜻을 출력함 
    print(k)
a[2024] = 6010#처음에 0으로 나오면 오류 생김
print(a)
for i in a.keys():
    print(i)
for i in a.items(): #쌍으로 출력함
    print(i)
print(a.get(2))
print(a.get(6010))#None값이 출력됌 이유는 key로 value 를 얻기 위한 함수이다.
#print(a[1])오류발생
print(a.get(1,10))#get(x,'디폴트 값')
print(a.get(1,'one'))
a[1] = 'one'
print(a.get(1,10)) #출력 one으로 됌
del a[1]
for i in a.keys():
    print(i)
#print(a[1]) 없으니깐...
