def funWithAnagrams(text):
    arr = []
    for i in range (len(text)):
        a = list(sorted(text[i]))
        a = "".join(a)
        arr.append(a)
    arr = list(set(arr))
    for i in range(len(arr)):
        print(arr[i])
    
x = int(input())
text = []
for i in range(x):
    temp = input()
    text.append(temp)

funWithAnagrams(text)