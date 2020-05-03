N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
R = B[0]
C = 0
for i in range(N):
    R += B[i+1]
    if A[i] >= R:
        C += R
    else:
        