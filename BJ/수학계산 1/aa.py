x = int(input())
count = 0
s = 0
while s < x:
    count +=1
    s += count
gap = s - x
if count % 2 == 1:
    mo = count - gap
    br = gap +1
else:
    br = count - gap
    mo = gap+1
print(f'{br}/{mo}')