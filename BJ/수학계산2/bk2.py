
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

m=int(input())
n=int(input())
d=[]
for i in range(m,n+1):
    if prime(i) == True:
       d.append(i)
    else:
        continue
if len(d) == 0:
    print(-1)
else:
    print(sum(d))
    print(min(d))

