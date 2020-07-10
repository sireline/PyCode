N, M = [int(n) for n in input().split()]
O = {i:[] for i in range(1, N+1)}
ans = [-1,-1] + [0]*(N-1)
print(O, ans)
for i in range(M):
    A, B = [int(n) for n in input().split()]
    O[A].append(B)
    O[B].append(A)
print(O)
idx = 1
while True:
    next_visit = O[idx]
    for v in next_visit:
        if ans[v] == 0:
            ans[v] = k
        print(ans)
    
