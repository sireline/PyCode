N, K = [int(n) for n in input().split()]
R, S, P = [int(n) for n in input().split()]
w = {'r': ('p', P), 's': ('r', R), 'p': ('s', S)}
T = list(input())
p = []
ans = 0
for i, c in enumerate(T):
    if i<K:
        ans += w[c][1]
        p.append(w[c][0])
    else:
        if p.pop(0)!=w[c][0]:
            ans += w[c][1]
            p.append(w[c][0])
        else:
            if i<N-K and w[T[i+K]][0]==w[c][0]:
                p.append(w[T[i+K]][0])
            else:
                p.append(c)
print(ans)
