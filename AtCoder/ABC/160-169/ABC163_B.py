N, M = [int(n) for n in input().split()]
A = sum([int(n) for n in input().split()])
print(N-A if A <= N else -1)
