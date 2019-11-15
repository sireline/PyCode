A,B=[int(n) for n in input().split()]
i=0
if B!=1:
    while B > 0:
        if i==0:
            B -= A
        else:
            B -= (A-1)
        i += 1
print(i)
