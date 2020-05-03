N, K, M = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
x = (M*N) - sum(A)
if -1 < x <=K:
    print(x)
elif x < 0:
    print(0)
else:
    print(-1)
