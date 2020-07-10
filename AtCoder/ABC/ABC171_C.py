N = int(input())
ans = []
alp = 'abcdefghijklmnopqrstuvwxyz'

def dfs(N):
    n, r = divmod(N-1, 26)
    ans.append(alp[r])
    if N <= 26:
        return (n, r)
    return dfs(n)

dfs(N)
print("".join(ans[::-1]))
