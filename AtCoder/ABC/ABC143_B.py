N = int(input())
d = [int(n) for n in input().split()]
ans = []
for i in range(N-1):
    for j in range(i+1, N):
        ans.append(d[i]*d[j])
print(sum(ans))
