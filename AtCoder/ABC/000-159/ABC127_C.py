N, M = [int(n) for n in input().split()]
L, R = (1, N)
for i in range(M):
    l, r = [int(n) for n in input().split()]
    L, R = (max(l, L), min(r, R))
print(max(0, R-L+1))
