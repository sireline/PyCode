N = int(input())
X = []
p = 0
for i in range(N):
    X.append(tuple([int(n) for n in input().split()]))
a = sorted(X)
while p<len(a)-1:
    if a[p][0]+a[p][1] > a[p+1][0]+a[p+1][1]:
        a.pop(p)
    elif  a[p][0]+a[p][1] > a[p+1][0]-a[p+1][1]:
        a.pop(p+1)
    else:
        p += 1
print(len(a))
