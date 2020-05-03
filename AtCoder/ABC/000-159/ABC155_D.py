from bisect import *

N, K = [int(n) for n in input().split()]
A = sorted([int(n) for n in input().split()])
i = bisect(A, 0)
print(A)
print(i)
if i==0:
    i = 1
    f = False
else:
    f = True
    j = 1
M = N - i
while M < K:
    if f:
        if j <= i:
            M += (N-i)
        else:
            M += (N-j)
        j += 1
    else:
        M += (N-i)
        i += 1    
print(j if f else  i, M)