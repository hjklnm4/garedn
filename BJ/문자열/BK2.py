n = int(input())
a = list(input())
b = list(map(int,a))
sum = 0
for i in range (len(b)):
    sum+=b[i]
print(sum)

