N, K, S = [int(n) for n in input().split()]
ans = []
for i in range(N-K):
    ans.append(S+1 if S<10**9 else 1)
for j in range(K):
    ans.append(S)
print(" ".join([str(n) for n in ans]))
