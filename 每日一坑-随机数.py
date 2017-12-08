import random
i = 1
while (i==1):
    a=int(input("输入最小值"))
    b=int(input("输入最大值"))
    c=int(input("输出取出的个数"))
    temp = random.sample(range(a,b),c)
    print(temp)
    j = int(input("是否继续？\n1-是\n2-否\n输入数字即可"))
    if j==1:
           i=1
    else:
           i=0

