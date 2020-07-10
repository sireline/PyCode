A, B, C, K = [int(n) for n in input().split()]
c = min(A, K)
K -= min(A, K)
if K==0:
    print(c)
else:
    K -= B
    if K==0:
        print(c)
    else:
        c -= K
        print(c)
