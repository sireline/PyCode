N, K = [int(n) for n in input().split()]

def n(x, n):
    return x * 2**(n-1)

ans =0
for i in range(1, N+1):
    j = 1
    while n(i, j) < K:
        j += 1
    ans += (1.0/N)*0.5**(j-1)
print(ans)