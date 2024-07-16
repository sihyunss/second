n,m = map(int,input().split())
sw = []
for _ in range(n):
    s = int(input())
    sw.append(s)
for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 1 :
        sw[b-1] = c
    elif a == 2 :
        for i in range(b-1,c):
            if sw[i] == 1:
                sw[i] = 0
            elif sw[i] == 0:
                sw[i] = 1
    elif a == 3:
        for i in range(b-1,c):
            sw[i] = 0
    elif a == 4:
        for i in range(b-1,c):
            sw[i] = 1

for r in sw:
    print(r,end = ' ')