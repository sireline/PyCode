N, A, B = [int(n) for n in input().split()]
if A == 0:
    print(0)
else:
    C, D = divmod(N, A+B)
    print(A*C+min(A, D))