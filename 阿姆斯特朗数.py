N = 10000  #定义寻找范围
num =[]        #阿姆斯特数存储数组
a1=a2=0        #用于判断前后步长
def getlist():      #定义函数用于获得阿姆斯特数
     for x in range(N+1):
          z=[]
          temp=0
          for j in str(x):              #将X转换为str型，进行循环输出做到将数字分解
               z.append(j)    #添加到临时列表
          for i in z:
               temp +=int(i)**len(str(x))    #利用临时列表长度判断X为几位数并计算其值
          if temp == x:
               num.append(x)       #将阿姆斯特数添加进存储列表    

def search_num():   #判断函数
     case = 0  #用于判断是否跳出循环
     a = int(input('输入一个数字'))
     for i in num:       #寻找一个比输入数字大的阿姆斯特数
          if i>a:
               t=num.index(i)      #获得目标数的位置
               case=1
          if case==1:         #跳出循环
               break
     a1=abs(num[t]-a)         #判断前后步长
     a2=abs(num[t-1]-a)
     if a1<a2:
          print(num[t])
     else:
          print(num[t-1])          #输出找到的阿姆斯特朗数

          

