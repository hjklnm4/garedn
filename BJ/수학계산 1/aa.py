x = int(input())
count = 0
s = 0
br , mo = 1
while s < x:
    count +=1
    s += count

if count % 2 == 1:
    br = count
else:
    mo = count

for i in range (x % count):
     
    