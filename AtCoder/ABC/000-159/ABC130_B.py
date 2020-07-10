from itertools import accumulate
from bisect import bisect

N, X = [int(n) for n in input().split()]
L = list(accumulate([0] + [int(n) for n in input().split()]))
print(bisect(L, X))
