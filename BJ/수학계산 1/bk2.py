
def ma(a):
  count  = 0
  s = 0
  while a > s :
      s += count * 6
      count += 1
      if a <= s+1:
          return count
          break

a = input()
a = int(a)
d=ma(a)
print (d)
   
