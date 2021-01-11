n = int(input())
a = 0

while True:
    if (n%5) == 0:
        a = a + (n//5)
        print(a)
        break
    n -=3
    a += 1
    if n < 0:
        print(-1)
        break