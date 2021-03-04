arr= [0 for i in range(10001)]
arr[1]=1
for i in range(2,98):
    for j in range(i*2,10001,i):
        arr[j]=1
n = int(input())
for i in range(n):
    a = int(input())
    b = a //2
    for j in range(b, 1 ,-1):
        if arr[j] == 0 and arr[a-j] ==0:
            print(j , a-j)
            break
    

