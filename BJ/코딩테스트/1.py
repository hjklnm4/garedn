def getNumber(arr):
    value = 1
    ans = 0
    for i in range (len(arr)):
        ans = ans + (arr[i] * value)
        value = value*2
    print(ans)
    
x  = int(input())
arr = []
for i in range (x):
    a = int(input())
    arr.append(a)
    
arr.reverse()
getNumber(arr)


