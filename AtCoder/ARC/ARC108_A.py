S, P = [int(n) for n in input().split()]
ans = 'No'
for n in range(1, int(P**0.5)+1):
    if P == (n*(S-n)):
        ans = 'Yes'
        break
print(ans)
