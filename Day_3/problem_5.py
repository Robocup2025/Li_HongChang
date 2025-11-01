y=int(input())
if y%400==0:
    flag=True
elif y%100==0:
    flag=False
elif y%4==0:
    flag=True
else:
    flag=False
if flag :
    print("yes")
else:
    print("no")