A = int(input())
B = int(input())
C = int(input())
D = list(str(A * B * C))
E = len(D)
nums = []
for i in range(10):
    nums.append(0)

for i in range(E) :
    if D[i] == '0' :
        nums[0]+=1
    elif D[i] == '1':
        nums[1]+=1
    elif D[i] == '2':
        nums[2]+=1
    elif D[i] == '3':
        nums[3]+=1
    elif D[i] == '4':
        nums[4]+=1
    elif D[i] == '5':
        nums[5]+=1
    elif D[i] == '6':
        nums[6]+=1
    elif D[i] == '7':
        nums[7]+=1
    elif D[i] == '8':
        nums[8]+=1
    elif D[i] == '9':
        nums[9]+=1  
for i in range(10):
    print(nums[i])

