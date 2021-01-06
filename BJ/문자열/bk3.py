a = list(input())
b = []
for i in range(97,123):
    j = chr(i)
    if j in a:
        b.append(a.index(j))
        continue
    else:
        b.append(-1)
for i in range (len(b)):
    print(b[i], end = ' ')