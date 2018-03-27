def hansu(a):
  num = int(a)
  if (num < 100):
    return 1
  else:
    one = num // 100
    two = num // 10 % 10
    three = num % 10
    if (one - two == two - three):
     return 1
    else:
     return 0

a = int(input())
count = 0
for i in range (a,0,-1):
  if (hansu(i)):
    count = count +1
print (count)

