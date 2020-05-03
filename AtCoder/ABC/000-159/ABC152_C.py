N = int(input())
P = [int(n) for n in input().split()]
c = 0
o = sorted([i for i in range(1, N+1)], reverse=True)
if o==P:
    print(N)
else:
    while P:
        r = min(P)
        P = P[:P.index(r)]
        c += 1
        print(P)
    print(c)
