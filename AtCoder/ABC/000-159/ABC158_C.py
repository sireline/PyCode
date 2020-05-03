A, B = [int(n) for n in input().split()]
XA = 100*A//8
XB = 10*B
r = abs(XA-XB)*0.1
print(-1 if r > 0.9 else max(XA, XB))
