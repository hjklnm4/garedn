a = str(input())
a = list(a.upper())

b=[]
c=list(set(a))
for i in set(a):
    b.append(a.count(i))
d=max(b)
e = []
for i in range (len(b)):
    if b[i] == d:
        if i != b.index(d):
           e.append(0)
        else:
            continue
if len(e)>0:
   print('?')
else:
    print(c[b.index(max(b))])
        

