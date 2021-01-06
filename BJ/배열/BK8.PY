C = int(input())


for i in range(C):
    a = list(map(int,input().split()))
    sum = 0
    for j in range(len(a)-1):
        sum += a[j+1]
    arr = sum / a[0]
    st = 0
    re = 0
    for k in range(len(a)-1):
        if a[k+1] > arr:
            st += 1
    re = (st/a[0]) * 100
    print(f'{re:.3f}%')

