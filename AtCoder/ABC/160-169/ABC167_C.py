N, M, X = [int(n) for n in input().split()]
C = []
A = []
for i in range(N):
    c, a = input().split(' ', 1)
    C.append(int(c))
    A.append([int(n) for n in a.split()])
A = [list(z) for z in zip(*A)]
print(C,A)
