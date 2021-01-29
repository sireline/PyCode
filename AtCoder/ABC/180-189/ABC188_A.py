X, Y = [int(n) for n in input().split()]
l = max(X, Y)
s = min(X, Y)
print('Yes' if s+3 > l else 'No')
