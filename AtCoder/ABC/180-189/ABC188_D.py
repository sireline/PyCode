N, P = [int(n) for n in input().split()]
ans = 0
sday = 10**9+1
mday = 0
T = []
for _ in range(N):
    T.append(tuple([int(n) for n in input().split()]))
    sday = min(sday, T[0])
    mday = max(mday, T[1])
print(sday, mday)
for i in range(sday, mday+1):
    p = 0
    for t in T:
        print(t, i, p)
        if t[0] <= i <= t[1]:
            p += t[2]
    if p > P:
        ans += P
    else:
        ans += p
print(ans)
