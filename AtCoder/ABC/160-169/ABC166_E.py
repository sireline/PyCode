from itertools import combinations

N = int(input())
A = [int(n) for n in input().split()]
ans = 0
for c in combinations(range(1, N+1), 2):
    if abs(c[0]-c[1]) == A[c[0]-1]+A[c[1]-1]:
        ans += 1
print(ans)
