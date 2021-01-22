from itertools import combinations
N = int(input())
d = 10**9+7
if N==1:
    ans = 0
elif N==2:
    ans = 2
else:
    ans = 0
    for i in range(1, N):
        print(len([c for c in combinations(range(N), i)]))
    ans = 2*(N-2)*9 % d
print(ans)