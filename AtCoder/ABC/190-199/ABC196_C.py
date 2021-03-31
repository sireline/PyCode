N = input()
l = len(N) % 2 
if l:
    N = '0' + N
l = len(N)//2

A = int(N[:l])
B = int(N[l:])
if A <= B:
    ans = A
else:
    ans = A-1 if A>9 else A
print(ans)