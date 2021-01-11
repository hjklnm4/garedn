
def cal(d):
    max = 0
    i = 1
    while (max < d):
        max = max + (i+1) //2
        i +=1
    return i -1

n = int(input())
for i in range (n):
    a,b = map(int,input().split())
    d = b-a
    
    print(cal(d))
    