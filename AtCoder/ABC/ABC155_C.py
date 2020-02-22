from collections import Counter

N = int(input())
c = Counter()
l = 0
for i in range(N):
    k = input()
    v = c.setdefault(k, 0)
    c[k] = v + 1
    if l < c[k]:
        l = c[k]
ans = sorted([k for k, n in c.items() if n==l])
[print(k) for k in ans]
