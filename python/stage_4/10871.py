a,b = input().split()
a = int(a)
b = int(b)
num = input().split()
for i in range (a):
  temp = int(num[i])
  if (temp < b):
    print (temp, end=' ')
print()

