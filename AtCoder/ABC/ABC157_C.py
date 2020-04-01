ans = [-1, -1, -1]
N, M = [int(n) for n in input().split()]
for i in range(M):
    s, c = [int(n) for n in input().split()]
    if N == 1:
        if s in [1, 2]:
            ans = -1
            break
        else:
            if ans[s-1] == -1 or c < ans[s-1]:
                ans[s-1] = c  
    elif N == 2:
        if s in [1]:
            ans = -1
            break
        else:
            if ans[s-1] == -1 or c < ans[s-1]:
                ans[s-1] = c  
    else:
        if ans[s-1] == -1 or c < ans[s-1]:
            ans[s-1] = c  
if len(ans) == 1:
    print(-1)
else:
    ans = "".join([str(c) for c in ans])
    if N == 3:
        if ans[0] == '-' or (ans[0] == '-' and ans[2] == '-'):
            print(-1)
            exit()
    elif N == 2:
        if ans[0] == '-' or ans[2] == '0':
            print(-1)
            exit()
    else:
        print(ans.replace('-1', '0'))
