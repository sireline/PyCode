N = int(input())
S = []
ans = 'satisfiable'
for i in range(N):
    S.append(input())
Ss = set(S)
for s in Ss:
    if s[0] != '!':
        if '!'+s in Ss:
            ans = s
            break
    else:
        if s[1:] in Ss:
            ans = s[1:]
            break
print(ans)
