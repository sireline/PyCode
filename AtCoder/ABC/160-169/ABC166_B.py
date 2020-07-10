N, K = [int(n) for n in input().split()]
o = {}
for i in range(1, N+1):
    o[i] = False
for j in range(K):
    d = int(input())
    for k in [int(n) for n in input().split()]:
        o[k] = True
print(list(o.values()).count(False))
