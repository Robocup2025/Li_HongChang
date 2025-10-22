str=input()
letter,digit,space,other=0,0,0,0
for char in str:
    if char=='\n':
        break
    elif char.isalpha():
        letter+=1
    elif char.isdigit():
        digit+=1
    elif char.isspace():
        space+=1
    else:
        other+=1
print(f"Letter:{letter} Digit:{digit} Space:{space} Other:{other}")