from bisect import bisect

X, N = [int(n) for n in input().split()]
if N==0:
    print(X)
else:
    P = sorted([int(n) for n in input().split()])
    if X not in P:
        print(X)
        exit()
    idx = bisect(P, X)
    ans_r = 101
    ans_l = 0
    for i in range(P[idx-1], 101):
        if i not in P:
            ans_r = i
            break
    for j in range(1, P[idx-1]):
        if j not in P:
            ans_l = j
    if abs(X-ans_l) == abs(ans_r-X):
        print(min([ans_l, ans_r]))
    else:
        print(ans_l if abs(X-ans_l) < abs(ans_r-X) else ans_r)
