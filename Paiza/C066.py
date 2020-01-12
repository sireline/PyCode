M, N, x = [int(n) for n in input().split()]
ans = 0
w = [int(input()) for _ in range(M)]
idx = 0
p = x
while N and idx < M:
    if p > w[idx]:
        p -= w[idx]
        ans += 1
        idx += 1
    else:
        N -= 1
        p = x
print(ans)
    