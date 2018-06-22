a = input()

num = [-1 for i in range(26)] 

for i in range (len(a)):
  temp = (ord(a[i])-97)
  if num[int(temp)] == -1:
    num[int(temp)] = i

for i in range(len(num)):
    print(num[i], end=' ')

print()


# this is wrong way to print
#for k in num:
#  print (num[k]) 
