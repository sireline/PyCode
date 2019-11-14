input_line = input()
for i,s in enumerate(input_line,1):
    if i%10==0:
        print(s)
    else:
        print(s,end="")
