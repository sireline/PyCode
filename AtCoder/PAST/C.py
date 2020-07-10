A, R, N = [int(n) for n in input().split()]
ans = A * R**(N-1)
print('large' if ans > 10**9 else ans)
