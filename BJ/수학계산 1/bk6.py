import math
t = int(input())

for i in range (t):
    k = int(input())
    n = int(input()) #k:층 n:호
    if k >=1 and n <=14:
        a=math.factorial(k+1)
        b=math.factorial(n-1)
        c= math.factorial(k+n)
        d = c//(a*b)

        print(d)
        
