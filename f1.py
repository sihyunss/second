def switch(switches, index):
    if switches[index] == 0:
        switches[index] = 1
    else:
        switches[index] = 0


num = int(input())
if num <= 100:
    sw = []
    
    sw = list(map(int, input().split()))
    student = int(input())
    
    for k in range(student):
        b, n = map(int, input().split())
        if b == 1:
            for i in range(n - 1, num, n):
                switch(sw, i)
        elif b == 2:
            n -= 1  
            switch(sw, n)
            left = n - 1
            right = n + 1
            while left >= 0 and right < num and sw[left] == sw[right]:
                switch(sw, left)
                switch(sw, right)
                left -= 1
                right += 1


for i in range(num):
    print(sw[i], end=' ')
