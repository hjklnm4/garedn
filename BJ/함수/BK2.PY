def d(n):
    next = n
    for i in list(str(n)):
        next += int(i)
    return next
p=[]
for i in range(10001):
    p.append(d(i))
p.sort()
for i in range(10001):
    if i in p:
        continue
    else:
        print(i)