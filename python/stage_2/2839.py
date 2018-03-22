a = int(input())

sum = 0

while True:
  if ( a == 0):
    print (int(sum))
    break

  if ( a <= 2):
    print (-1)
    break

  if (a%5 != 0):
    a = a - 3
    sum = sum + 1
  else:
    sum = sum + int(a/5)
    a = 0

