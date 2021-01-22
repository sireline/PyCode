a, b, c, d = [int(n) for n in input().split()]
ans = {0:b*d, 2:b*d, 3:a*d, 8:b*d, 10:max(a*c, b*d), 11:a*c, 12:b*c, 14:a*c, 15:a*c}
f = 0
if a<0:
    f += 8
if b<0:
    f += 4
if c<0:
    f += 2
if d<0:
    f += 1
print(ans[f])
