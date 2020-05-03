N, M =[int(n) for n in input().split()]
p = {}
s = {}
for i in range(M):
    P, S = input().split()
    if S=='WA' and P not in p:
        c = s.setdefault(P, 0)
        c += 1
        s[P] = c
    else:
        if not p.setdefault(P, 0):
            p[P] = 1
for k in s:
    if k not in p:
        s[k] = 0 
print(sum(p.values()), sum(s.values()))
