N = int(input())
P = [int(n) for n in input().split()]
X = [n for n in range(1, N+1)]
ans = sum([0 if p==x else 1 for p,x in zip(P, X)])
print('YES' if ans <= 2 else 'NO')
