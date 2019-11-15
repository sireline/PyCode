N=int(input())
A=[int(n) for n in input().split()]
B=[int(n) for n in input().split()]
C=[int(n) for n in input().split()]
ans = 0
pre = -1
for i in A:
    ans += B[i-1]
    if pre == i-1:
        ans += C[i-2]
    pre = i
print(ans)
