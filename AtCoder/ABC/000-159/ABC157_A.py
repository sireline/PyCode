ans = 'No'
A = []
for _ in range(3):
    A.append([int(n) for n in input().split()])
N = int(input())
B = []
for i in range(N):
    B.append(int(input()))
for n in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == n:
                A[i][j] = 0
for a,b,c in zip(A[0], A[1], A[2]):
    if sum([a,b,c]) == 0:
        ans = 'Yes'
for i in range(3):
    if sum(A[i]) == 0:
        ans = 'Yes'
if sum([A[0][0], A[1][1], A[2][2]]) == 0:
    ans = 'Yes'
if sum([A[0][2], A[1][1], A[2][0]]) == 0:
    ans = 'Yes'
print(ans)
