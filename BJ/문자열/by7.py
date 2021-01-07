a,b = map(str,input().split())
a = list(a)
a.reverse()
c =int(''.join(a))
b = list(b)
b.reverse()
d=int(''.join(b))
if c >d:
    print (c)
else:
    print(d)

