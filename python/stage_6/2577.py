a = int(input())
b = int(input())
c = int(input())

num = a * b * c

arr = [0]*10

while True:
  if (num >= 10):
    temp = num % 10
    arr[temp] = arr[temp] + 1
    num = num // 10
  else:
    arr[num] = arr[num] + 1
    break

for i in range (10):
  print (arr[i])




