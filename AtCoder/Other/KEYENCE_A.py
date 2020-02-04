H = int(input())
W = int(input())
N = int(input())
a = max(H, W)
c = 0
ans = 0
while N > c:
    c += a
    ans += 1
print(ans)
