N = int(input())
A = sorted([int(n) for n in input().split()], reverse=True)
M = 10**18
ans = A[0]
for i in range(1, len(A)):
    if A[-1] == 0:
        ans = 0
        break
    ans *= A[i]
    if M < ans:
        ans = -1
        break 
print(ans)
