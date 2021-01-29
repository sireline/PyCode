N = int(input())
ans = 0
XY = []
for _ in range(N):
    x, y = [int(n) for n in input().split()]
    XY.append((x, y))
for i in range(N-1):
    for j in range(i+1, N):
        dydx = (XY[j][1]-XY[i][1]) / (XY[j][0]-XY[i][0])
        if -1 <= dydx <= 1:
            ans += 1
print(ans)
