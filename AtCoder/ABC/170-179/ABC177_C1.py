from itertools import combinations

N = int(input())
A = [int(n) for n in input().split()]
print(sum([i*j for i,j in combinations(A, 2)])%(10**9+7))