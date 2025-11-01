list=list(range(1,234))
idx=0
while len(list)>2:
    idx=(idx+2)%len(list)
    list.pop(idx)
print(list)