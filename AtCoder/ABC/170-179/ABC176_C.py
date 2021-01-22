N = int(input())
A = [int(n) for n in input().split()]
m = A[0]
ans = 0
for i in range(1, N):
    if m > A[i]:
        ans += (m-A[i])
    else:
        m = A[i]
print(ans)
