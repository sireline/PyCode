from itertools import combinations

while True:
    n, x = [int(n) for n in input().split()]
    if n==x==0:
        break
    print(sum([1 for t in combinations(range(1, n+1), 3) if sum(t) == x]))
