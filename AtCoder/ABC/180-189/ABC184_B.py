N, X = [int(n) for n in input().split()]
S = input()
for s in S:
    if s=='o':
        X += 1
    elif X > 0:
        X -= 1
print(X)
