N, K = [int(n) for n in input().split()]
ans = []
while 0<N:
    N, m = divmod(N, K)
    ans.append(m)
print(len(ans))