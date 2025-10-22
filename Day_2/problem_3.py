H=100
sum=H
h=H/2
for i in range(9):
    sum+=h*2
    h/=2
print(f"The sum of the heights of the top ten times is {sum}m.")
print(f"The tenth height is {h}m.")