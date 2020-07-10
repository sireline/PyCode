N, M, Q = [int(n) for n in input().split()]
a, b, c, d = [list(x) for x in zip(*[[int(n) for n in input().split()] for _ in range(Q)])]
ans = 0

def dfs(A):
    global ans
    if len(A) == N:
        now = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]: now += d[i]
        ans = max(ans, now)
        return

    for v in range(A[-1], M+1):
        A.append(v)
        dfs(A)
        A.pop()

dfs([1])
print(ans)
