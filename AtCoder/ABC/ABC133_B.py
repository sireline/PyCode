from itertools import combinations

N, D = [int(n) for n in input().split()]
X = []
for i in range(N):
    X.append([int(n) for n in input().split()])
ans = 0
for i, j in combinations(X, 2):
    if (sum([(j[d]-i[d])**2 for d in range(D)])**0.5).is_integer():
        ans += 1
print(ans)
