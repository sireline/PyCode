N = int(input())
H = [int(n) for n in input().split()]
m = H[N-1]
ans = 'Yes'
for i in range(0, N-1)[::-1]:
    if H[i] > m+1:
        ans = 'No'
        break
    elif H[i] == m+1:
        m = H[i]-1
    else:
        m = H[i]
print(ans)
