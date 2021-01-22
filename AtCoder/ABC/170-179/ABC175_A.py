#N, M = [int(n) for n in input().split()]
#N = int(input())
S = input()
ans = 0
r = 0
for c in S:
    if c == 'R':
        r += 1
        ans = r
    else:
        ans = max(ans, r)
        r = 0
print(ans)
