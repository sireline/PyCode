K, X = [int(n) for n in input().split()]
print(" ".join([str(n) for n in range(X-(K-1), X+(K))]))
