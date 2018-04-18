a = int(input())

for i in range (a):
  temp = input()
  size = len(temp)
  score = 0
  bonus = 0
  for j in range(size):
    if (temp[j] == 'O'):
      bonus = bonus + 1
      score = score + bonus
    else:
      bonus = 0
  print (score)

