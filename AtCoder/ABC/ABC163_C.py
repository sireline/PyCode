from itertools import zip_longest
N = int(input())
A = [int(n) for n in input().split()]
o  = {}
for a in A:
    o[a] = o.setdefault(a, 0)+1
[print(o[k] if idx==k else 0) for idx, k in zip_longest(range(1, N+1), o.keys())]
