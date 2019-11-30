N = int(input())
l = 100.0
r = 200.0
for i in range(N):
    c, h = input().split()
    h = float(h)
    if c == 'le':
        if h < r:
            r = h
    else:
        if h > l:
            l = h
print(l, r)
