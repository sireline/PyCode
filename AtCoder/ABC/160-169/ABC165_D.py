A, B, N = [int(n) for n in input().split()]
ans = []
for x in range(1, A):
    ans.append((A*x//B)-A*(x//B))
print(max(ans))
