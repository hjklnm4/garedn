n = int(input())
def X(n):
    re = 0
    for j in range(1,n+1):
        a = list(str(j))
        b = list(map(int,a))
        if len(b) <= 2:
            re += 1
        else:
            for i in range (len(b)-2):
                if (b[i+2]-b[i+1])==(b[i+1]-b[i]):
                    re+=1
                else:
                    break
    print(re)  
X(n)
