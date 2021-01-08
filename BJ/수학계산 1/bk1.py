a,b,c = map(int,input().split())


def arr(a,b,c):
    d = 0
    re = 0
    if b >= c :
        return -1
    else :
        return int(a/(c-b)+1)

d = arr(a,b,c)
print(d)