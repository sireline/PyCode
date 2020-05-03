from itertools import combinations

N, M = [int(n) for n in input().split()]
print(len([c for c in combinations(range(N), 2)])+len([c for c in combinations(range(M), 2)]))