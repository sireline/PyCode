N, D = [int(n) for n in input().split()]
ans = 0
for i in range(N):
    X, Y = [int(n) for n in input().split()]
    if (X**2+Y**2)**0.5 <= D:
        ans += 1
print(ans)
