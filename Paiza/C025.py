import math

M = int(input())
N = int(input())
O = {}
z = 0
for i in range(N):
    x, y, c = [int(n) for n in input().split()]
    if x not in O:
        O.setdefault(x, c)
    else:
        O[x] += c
for k, v in O.items():
    z += math.ceil(v / M)
print(z)
