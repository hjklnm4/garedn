a = int(input())
sum = 0
b = [str(input().lower()) for _ in range(a)]

for i in b:
    result =0
    for j in range (len(i)):
        if i.find(i[j],j+1) -j > 1 :
            result = -1
            break
        else:
            result = 1
            continue
    if result == 1:
        sum +=1
    else :
        continue
print(sum)  