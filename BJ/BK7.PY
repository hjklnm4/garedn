n = int(input())
nums = []
arr = []

b = [input() for _ in range(n)]
for i in range(len(b)):
    c = list(b[i])
    sum = 0
    reset = 0
    for j in range(len(c)):
        if c[j] == 'O':
            reset += 1
        else:
            reset = 0
        sum += reset
    print(sum)