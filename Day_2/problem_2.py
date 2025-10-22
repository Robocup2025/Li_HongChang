a=input("Please input a number:")
n=int(input("Please input the cycle indix:"))
str=''
sum=0
for i in range(n):
    str+=a
    sum+=int(str)
print("The sum is:",sum)