A = [int(n) for n in input().split()]
ans = 'No'
if A[0] == A[1]+A[2]+A[3]:
    ans = 'Yes'
if A[1] == A[0]+A[2]+A[3]:
    ans = 'Yes'
if A[2] == A[0]+A[1]+A[3]:
    ans = 'Yes'
if A[3] == A[0]+A[1]+A[2]:
    ans = 'Yes'
if A[0]+A[1] == A[2]+A[3]:
    ans = 'Yes'
if A[0]+A[2] == A[1]+A[3]:
    ans = 'Yes'
if A[0]+A[3] == A[1]+A[2]:
    ans = 'Yes'
print(ans)