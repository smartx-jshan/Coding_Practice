import sys

n = int(input())

X = int(n)
Y = int(n/3 * 5 + (n/3-1))

arr = [[' ' for col in range(Y)] for row in range(X)]

count = 0


def star (height, x, y):

  global count
  count = count +1
  if (height == 3):
    arr[x][y]= '*'
    arr[x+1][y-1] = '*'
    arr[x+1][y] =' '
    arr[x+1][y+1] ='*'
    arr[x+2][y-2] ='*'
    arr[x+2][y-1] ='*'
    arr[x+2][y] ='*'
    arr[x+2][y+1] ='*'
    arr[x+2][y+2] ='*'
    return

  star (int(height/2), x,  y)
  star (int(height/2), x + int(height/2) , y - int(height/2))
  star (int(height/2), x + int(height/2) , y + int(height/2))

def pr(x,y):
  for i in range (x):
    for j in range(y):
       sys.stdout.write(arr[i][j])
    print()  

star (n,0,n-1)

pr(X,Y)

print ("Count number: ", count)
 
 
