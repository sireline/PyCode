N = int(input())
X = []
for i in range(1, N+1):
    s, p = input().split()
    X.append((s, int(p), i))
ans = sorted([(k,v,i) for k,v,i in X], key=lambda x: (x[0], -x[1]))
[print(x[2]) for x in ans]
