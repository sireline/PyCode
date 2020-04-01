N = int(input())
ans = 0
for i in range(1, N+1, 2):
    c = 0
    p = []
    for j in range(1, i+1):
        if i%j == 0:
            p.append(j)
            c += 1
    if c == 8:
        ans += 1
        print(i)
        print(p)
print(ans)
