H, W, X, Y = [int(n) for n in input().split()]
S = []
ans = 0
cnt = 0
for i in range(H):
    S.append(list(input()))
for i in range(H):
    if S[i][Y-1] == '.':
        ans += 1
    elif i < X-1:
        ans = 0
    else:
        break
for j in range(W):
    if S[X-1][j] == '.':
        cnt += 1
    elif j < Y-1:
        cnt = 0
    else:
        break
print(ans+cnt-1)
