N, R = [int(n) for n in input().split()]
print(R+(100*(10-N)) if N<10 else R)
