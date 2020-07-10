N, K = [int(n) for n in input().split()]
print(min(N%K, K-(N%K)))