import numpy as np
from math import factorial

D = 10**9+7
N, K = [int(n) for n in input().split()]
C = []
CO = {}
E = []
for i in range(1, N+1):
    C.append(i)
    CO[i] = 0
a = [int(n) for n in input().split()]
for i in range(K):
    R = np.random.choice(C, a[i], replace=False)
    nCk = factorial(N) // (factorial(a[i]) * factorial(N-a[i]))
    E.append(nCk)
    for r in R:
        CO[r] += 1
h = 1
for v in CO.values():
    h *= v
ee = 1
for e in E:
    ee *= e
print(h*ee%D)
