N, S, D = [int(n) for n in input().split()]
ans = 'No'
for i in range(N):
    x, y = [int(n) for n in input().split()]
    if x >= S or y <= D:
        continue
    else:
        ans = 'Yes'
print(ans)