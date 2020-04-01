N = int(input())
X = sorted([int(n) for n in input().split()])
ans = 10**9
for p in range(X[0], X[-1]+1):
    c = 0
    for x in X:
        c += (x-p)**2
    if c < ans:
        ans = c
print(ans)