X, K, D = [int(n) for n in input().split()]
x = abs(X)
d = (x+D-1)//D
r = x % D
ans = 0
if d<=K:
    if X>0:
        X -= d*D
    else:
        X += d*D
    K -= d
    if K%2==0:
        ans = X
    else:
        if X>0:
            ans = X-D
        else:
            ans = X+D
else:
    if X>0:
        ans = X-K*D
    else:
        ans = X+K*D
print(abs(ans))
