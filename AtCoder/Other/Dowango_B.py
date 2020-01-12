import numpy as np

N = int(input())
x = [int(n) for n in input().split()]
for i in range(N-1):
    k = np.random.randint(1, N-i, 1)
    print(k)
    x[k]
