N, M = [int(n) for n in input().split()]
o = {}
for i in range(1, N+1):
    o[i] = []
for j in range(M):
    x, y = [int(n) for n in input().split()]
    o[x].append(y)
    o[y].append(x)
for i in range(1, N+1):
    print(i, set(o[i]))
