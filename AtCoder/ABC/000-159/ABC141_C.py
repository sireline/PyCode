N, K, Q = [int(n) for n in input().split()]
c = {}
ans = [K]*N
for i in range(Q):
    a = int(input())
    if a not in c:
        c.setdefault(a, 1)
    else:
        c[a] += 1
for j in range(N):
    print('Yes' if ans[j] - (Q-c.get(j+1, 0)) > 0 else 'No')
