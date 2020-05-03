N = int(input())
W = [int(n) for n in input().split()]
ans = 100*100
for i in range(1, N):
    ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
print(ans)
