import numpy as np
from math import factorial

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

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
    nCk = cmb(N, a[i], mod)
#    nCk = factorial(N) // (factorial(a[i]) * factorial(N-a[i]))
    E.append(nCk)
    for r in R:
        CO[r] += 1
h = 1
for v in CO.values():
    h *= v
ee = 1
for e in E:
    ee *= e
print(h*ee)
