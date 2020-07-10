N = int(input())
H = [int(n) for n in input().split()][::-1]
print(H)
ans = 1
for i in range(N-1):
    f = False
    for j in range(i+1, N):
        if H[i] <= H[j]:
            f = True
    if f:
        ans += 1
print(ans)
