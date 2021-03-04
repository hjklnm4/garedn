
def prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2,x):
            if (x%n)==0:
                return False
                break
            else:
                continue
        return True

n=int(input())
d=[]
count =0

while n != 0:
    d.append(n)
    if n == 0 :
        break
    else:
        n = int(input())
        continue

for i in range(len(d)):
    for j in range(i, i*2+1):
        if prime(d[i]) == True:
            count+=1
        else:
            continue
    print(count)



