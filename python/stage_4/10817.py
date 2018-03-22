a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a == b):
  print (a)
elif (a > b):
  if (a <= c):
    print (a)
  elif (c <= b):
    print (b)
  else:
    print (c)
else:
  if (b <= c):
    print (b)
  elif (c <= a):
    print (a)
  else:
    print (c)

