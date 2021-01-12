
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

a=int(input())
b=list(map(int,input().split()))
d=0
for i in range(a):
    if prime(b[i]) == True:
       d+=1
    else:
        continue
print(d)


        

