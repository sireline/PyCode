N = int(input())
A = [int(n) for n in input().split()]
ans = 0
s = 0
for i,a in enumerate(A[::-1],1):
    s += a
    ans += A[-i]*s
print(ans%(10**9+7))
