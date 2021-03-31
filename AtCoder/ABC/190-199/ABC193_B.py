N = int(input())
m = 10**9+1
ans = -1
for i in range(N):
    A, P, X = [int(n) for n in input().split()]
    if X-A>0:
        m = min(m, P)
print(ans if m == 10**9+1 else m)