N = int(input())
cate = {0: 5, 1: 3, 2: 2, 3: 1}
o = {}
ans = []
for i in range(N):
    v , p = [int(n) for n in input().split()]
    o[v] = o.setdefault(v, 0) + p
for v, p in o.items():
    ans.append(p//100 * cate[v])
print(sum(ans))
