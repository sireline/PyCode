N, M = [int(n) for n in input().split()]
A = sorted([int(n) for n in input().split()], reverse=True)
print('Yes' if len([m for m in A if m >= sum(A)/(4*M)]) >= M else 'No')
