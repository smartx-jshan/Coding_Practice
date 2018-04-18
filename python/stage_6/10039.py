a = list (range(5))

for i in range (5):
  a[i] = int(input())

sum = 0

for i in range(5):
  if (a[i] <=40):
    sum = sum + 40
  else:
    sum = sum + a[i]

print (int(sum /5))
