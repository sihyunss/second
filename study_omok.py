
"""
omok = [[['-' for _ in range(3)] for _ in range(3)] for _ in range(3)]


omok[0][2]='x'
omok[0][0] = 'o'
omok[0][1]='x'
omok[1][2] = 'o'
omok[2][2] ='x'
print(omok)
print(omok[1][1])
print(omok[0][2])
for i in range(3):
    for j in range(3):
        print(omok[i][j],end=' ')
    print()
for i in omok[0][range(3)]:
    print(i,end=' ')
print()
for i in omok[1][range(3)]:
    print(i,end=' ')
print()
for i in omok[2][range(3)]:
    print(i,end=' ')
print()

# Initialize the 3D list (3x3x3)
omok = [['-' for _ in range(3)] for _ in range(3)]

# Modify specific elements
omok[0][2] = 'x'
omok[0][0] = 'o'
omok[0][1] = 'x'
omok[1][2] = 'o'
omok[2][2] = 'x'

print(omok)
for i in range(3):
    for j in range(3):
        print(omok[i][j],end =' ')
    print()
    """
n = 0
while True:
    n +=1
    if n==10:
        break
    if n %2 == 0:
        continue
    
    print(n)