from itertools import combinations

N = int(input())
A = [int(n) for n in input().split()]

print(*[x for x in combinations(A, 2) if x[0]*x[1]%4==0])
print('Yes' if len([x for x in combinations(A, 2) if x[0]*x[1]%4==0]) >= N-1 else 'No')
