N = int(input())
X = []
p = 0
for i in range(N):
    x, l = [int(n) for n in input().split()]
    X.append((x-l, x, x+l))
a = sorted(X, key=lambda x: x[1])
while p<len(a)-1:
    if a[p][1] > a[p+1][1]:
        a.pop(p)
    elif  a[p][1] > a[p+1][0]:
        a.pop(p+1)
    else:
        p += 1
print(len(a))
