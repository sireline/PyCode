A, B, X = [int(n) for n in input().split()]
l, r = 0, 10**9+1

while l+1 < r:
    N = (l+r) // 2
    print(l,r,N, A*N+B*len(str(N)))
    if A * N + B * len(str(N)) > X:
        r = N
    else:
        l = N
print(l)