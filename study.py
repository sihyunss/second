a = 'x^2+x-2=0'
if 'x^2' in a:
    print('ok')
a = 'x^2+x-2=0'
if 'x^2' not in a:
    print('이 방정식은 2차 방정식이 아닙니다.')
else:
    print('이 방정식은 2차 방정식입니다.')
a = '6x^2'
index=a.find('x^2')
if '0'<=a[0:index]<='100':
    print(a.find('0'<=a[0:index]<='100'))
if 'x^2' in a[0:3]:
    print('ok')
else : 
    print('숫자 있음')

if '0'<=a[0]<='1000':
    print(a[0])
else :
    print('오류')
if a[0] == '-':
    print('-')
else :
    print('+')

dict = '10x^2+x-2=0'
if '0'<=a[0]<='1000':
    b = a[0:5]
    print(b-'x^2')
num = 1

"""while True:
    if dict[num] == 'x':
        if dict[0] =='x':
            a = 1
        int(a)
        break
    a= dict[num]
    num +=1
print(a)
"""
while True :
    if dict[num] =='x':
        break
    num+=1
print(int(dict[0:num]))
print(int(-10)+10)
