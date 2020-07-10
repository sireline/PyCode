from itertools import accumulate
from bisect import bisect_right

N, M, K = [int(n) for n in input().split()]
A = [0]+[*accumulate([int(n) for n in input().split()])]
B = [*accumulate([int(n) for n in input().split()])]
ans = 0
a = bisect_right(A, K)
for i in range(a):
    b = bisect_right(B, K-A[i])
    ans = max(ans, i+b)
print(ans)
