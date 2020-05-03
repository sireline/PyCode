from itertools import permutations

N = int(input())
P = tuple(int(n) for n in input().split())
Q = tuple(int(n) for n in input().split())

a = [x for x in permutations(range(1,N+1), N)]

print(abs(a.index(P)-a.index(Q)))
