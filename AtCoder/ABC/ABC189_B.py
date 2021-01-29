N, X = [int(n) for n in input().split()]
ans = -1
x = 0
for i in range(1, N+1):
    v, p = [int(n) for n in input().split()]
    x += v * p
    if x > X*100:
        ans = i
        break
print(ans)
