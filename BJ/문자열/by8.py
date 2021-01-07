a = list(input())
sum = 0
for i in range(len(a)):
    a[i]=ord(a[i])
    if 65<=a[i] and a[i]<=67: 
        sum += 3
    elif 68<=a[i] and a[i]<=70: 
        sum += 4
    elif 71<=a[i] and a[i]<=73:
        sum += 5
    elif 74<=a[i] and a[i]<=76: 
        sum += 6
    elif 77<=a[i] and a[i]<=79: 
        sum += 7
    elif 80<=a[i] and a[i]<=83: 
        sum += 8
    elif 84<=a[i] and a[i]<=86: 
        sum += 9
    elif 87<=a[i] and a[i]<=90: 
        sum += 10
    else:
        print("타입에러")
print(sum)
