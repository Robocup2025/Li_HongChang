import math


for n in range(101,200):
    flag=True
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            flag=False
            break
    if flag:
        print(n)