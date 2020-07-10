from itertools import combinations_with_replacement
N, M, Q = [int(n) for n in input().split()]
X = [[int(n) for n in input().split()] for _ in range(Q)]
print(X)
ans = 0
for A in combinations_with_replacement(range(1, M+1), N):
    print(A)
    t = 0
    for x in X:
        if A[x[1]-1]-A[x[0]-1] == x[2]: t += x[3]
    ans = max(ans, t)
print(ans)
