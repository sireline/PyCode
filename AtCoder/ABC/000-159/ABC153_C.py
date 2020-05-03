N, K = [int(n) for n in input().split()]
H = sorted([int(n) for n in input().split()], reverse=True)
print(sum(H[K:]))
