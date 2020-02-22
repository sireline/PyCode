N, K = [int(n) for n in input().split()]
P =  [int(n) for n in input().split()]
q = []
#o = {}
#for i in range(1,1001):
#    o[i] = sum([(j/i) for j in range(1,i+1)])
ans = 0
for k in range(N-K):
    if k==0:
        for x in P[k:k+K]:
            q.append(sum([(j/x) for j in range(1,x+1)]))
        print(q)
    else:
        q.append(sum([(j/P[k+K]) for j in range(1,P[k+K])]))
    m = sum(q)
    q.pop(0)
    if m > ans:
        ans = m
print(ans)
    