from itertools import combinations

N, K = [int(n) for n in input().split()]
div = 10**9+7
ans = []
for k in range(K, N+2):
    ans += [(k*10**100+sum(c))%div for c in combinations(range(N+1), k)]
print(len(set(ans)))
