K, N = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
A += [A[0]+K]
dx = []
for i in range(N):
    dx.append(A[i+1] - A[i])
print(K-max(dx))
