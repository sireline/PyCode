from itertools import product

N, M = [int(n) for n in input().split()]
AB = [tuple([int(n) for n in input().split()]) for _ in range(M)]
K = int(input())
CD = [tuple([int(n) for n in input().split()]) for _ in range(K)]
ans = 0
for balls in product(*CD):
    balls = set(balls)
    cnt = sum(1 for A, B in AB if A in balls and B in balls)
    if ans < cnt:
        ans = cnt
print(ans)
