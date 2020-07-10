N, M = [int(n) for n in input().split()]
H = [int(n) for n in input().split()]
ans = ['G']*N
for i in range(M):
    AB = tuple([int(n) for n in input().split()])
    if H[AB[0]-1] == H[AB[1]-1]:
        ans[AB[0]-1] = -1 if ans[AB[0]-1]!= (1 or 0) else ans[AB[0]-1]
        ans[AB[1]-1] = -1 if ans[AB[1]-1]!= (1 or 0) else ans[AB[1]-1]
    elif H[AB[0]-1] > H[AB[1]-1]:
        ans[AB[0]-1] = 1
        ans[AB[1]-1] = -1
    else:
        ans[AB[0]-1] = -1
        ans[AB[1]-1] = 1
print(ans.count(0)+ans.count(1)) 
