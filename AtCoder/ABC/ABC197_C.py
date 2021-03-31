N = int(input())
A = [int(n) for n in input().split()]
ans = 10**30
for i in range(1, N):
    fans = 0
    bans = 0
    for a in A[:i]:
        fans |= a
    for b in A[i:]:
        bans |= b
    ans = min(ans, fans^bans)
print(ans)
