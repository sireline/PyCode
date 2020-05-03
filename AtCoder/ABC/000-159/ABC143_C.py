N = int(input())
S = input()
c = S[0]
ans = [S[0]]
for i in range(1, N):
    if c != S[i]:
        c = S[i]
        ans.append(c)
print(len(ans))
