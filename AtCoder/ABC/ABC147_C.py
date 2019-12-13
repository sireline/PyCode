N = int(input())
A = {}
for i in range(N):
    A[i] = []
    for j in range(int(input())):
        A[i].append([int(n) for n in input().split()])
    