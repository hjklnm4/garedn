n = 10
a = [int(input()) for _ in range(n)]
nums = []


for i in range(10):
    nums.append(0)

for j in range(10):
    nums[j] = a[j] % 42 
nums = set(nums)
print(len(nums))
       
            
