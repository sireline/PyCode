N = int(input())
ans = []
for i in range(N):
    a, b = [int(n) for n in input().split()]
    for n in range(a, b+1):
        ans.append(n) 
print(sum(ans))
