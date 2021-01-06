a = int(input())
arr = []
y = []
for i in range(a):
    tmp = list(map(str,input().split()))
    arr.append(tmp)

for x,y in arr:
    for i in range(len(y)):
        print(y[i]*int(x),end='')
    print('')
    
        
            
        
    



