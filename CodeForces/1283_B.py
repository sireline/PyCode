t = int(input())
for i in range(t):
    n, k = [int(n) for n in input().split()]
    print(n//k*k + min(n%k, k//2))
