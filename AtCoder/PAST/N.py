N, Q = [int(n) for n in input().split()]
A = [i for i in range(1, N+1)]
for i in range(Q):
    t, x, y = [int(n) for n in input().split()]
    if t==1:
        A[x-1], A[x] = A[x], A[x-1]
    else:
        A = A[:x-1] + sorted(A[x-1:y]) + A[y:]
print(*A)
