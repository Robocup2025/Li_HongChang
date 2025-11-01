#.pop方法修改了列表list,导致list[idx]不是原本希望的值，并造成了列表索引越界
#修改如下：
if __name__ == "__main__":
    list = list(range(1000))
    idx=0
    while idx<len(list):
        if list[idx] % 2 == 1:
            list.pop(idx)
        else:
            idx+=1
    print(list)