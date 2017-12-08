import random
N=4
x=0
for i in range(0,N):
     a = random.sample('1234',3)
     for j in a:
          print(j,end='')
     x=x+1
     print('x',x)
