N = int(input())
S = input()
O = {'R':[], 'G':[], 'B':[]}
for i,c in enumerate(S):
    O[c].append(i)
ans = len(O['R'])*len(O['G'])*len(O['B'])
for i in O['R']:
    for j in O['G']:
        for k in O['B']:
            m = sorted([i,j,k])
            if m[2]-m[1] == m[1]-m[0]:
                ans -= 1
print(ans)
