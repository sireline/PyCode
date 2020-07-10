X = int(input())
ans = 0
while True:
    if X < 5:
        break
    if X >= 500:
        v, r = divmod(X, 500)
        ans += v * 1000
        X = r
    if X >= 5:
        v, r = divmod(X, 5)
        ans += v * 5
        X = r
print(ans)