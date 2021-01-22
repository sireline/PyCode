S = input()
ew = 0
ow = 0
eb = 0
ob = 0
for i,c in enumerate(S):
    if i%2:
        if c=='0':
            ob += 1
        else:
            ow += 1
    else:
        if c=='0':
            eb += 1
        else:
            ew += 1
print(eb,ow, ew, ob)
print(f'Even:0=> {ew + ob}')
print(f'Even:1=> {eb + ow}')