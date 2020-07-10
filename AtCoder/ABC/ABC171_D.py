from collections import Counter
from decimal import *

N = int(input())
dp = [0]*(10**5+1)
A = []
for n in input().split():
    n = int(n)
    dp[n] += 1
    A.append(n)
ans = sum(A)
Q = int(input())
for _ in range(Q):
    B, C = [int(n) for n in input().split()]
    diff = dp[B] * (C-B)
    ans += diff
    print(ans)
    dp[C] += dp[B]
    dp[B] = 0
