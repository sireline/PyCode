N, M = [int(n) for n in input().split()]
A = [[int(n) for n in input().split()] for _ in range(N)]
B = [int(input()) for _ in range(M)]
[print(sum([x*y for x,y in zip(a, B)])) for a in A]
