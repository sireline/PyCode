from decimal import *
import math

N = int(input())
A = []
ans = 0
for _ in range(N):
    A.append(Decimal(input()))
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        if math.modf(A[i]*A[j])[0] == 0:
            print(A[i],A[j],A[i]*A[j])
            ans += 1
print(ans)
