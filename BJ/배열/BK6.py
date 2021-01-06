n = int(input())
sum = 0

a = list(map(int, input().split()))
m = max(a)

for i in range(len(a)):
    a[i] = a[i]/m*100

for i in range(len(a)):
    sum += a[i]
arr = sum / n
print(arr)