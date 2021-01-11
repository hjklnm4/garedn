a = int(input())
for i in range(a):
    h , w , p = map(int,input().split()) 
    if p % h !=0:
        x = p%h
        y = int(p/h) + 1
    else:
        x = h
        y = int(p/h)
    if y >= 10:
        print(f'{x}{y}')
    else:
        print(f'{x}0{y}')
    