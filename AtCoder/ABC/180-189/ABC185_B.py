N, M, T = [int(n) for n in input().split()]
AB = N
p = 0
ans = 'Yes'
for m in range(M):
    a, b = [int(n) for n in input().split()]
    AB -= (a-p)
    if AB <= 0:
        ans = 'No'
        break
    AB = min(AB+(b-a), N)
    p = b
if AB - (T-b) <= 0:
    ans = 'No'
print(ans)