import bisect

N = int(input())
L = int(''.join([str(n) for n in range(1, N+1)]))
R = int(''.join([str(n) for n in range(1, N+1)][::-1]))

P = int(''.join(input().split()))
Q = int(''.join(input().split()))

C = [str(c) for c in range(1, N+1)]
A = []
for i in range(L, R+1):
    flg = True
    for c in C:
        if c not in str(i):
            flg = False
            break
    if flg:
        A.append(i)
print(abs(bisect.bisect(A, P)-bisect.bisect(A, Q)))
