a, b, v = map(int,input().split())

d = (v-a)/(a-b)
if type(d) == float and int(d) == d:
    print (int(d+1))
else:
    print(int(d+2))