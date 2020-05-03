def combi(n, r):
    p = 1
    for i in range(1, r+1):
        p = p * (n-i+1) // i
    return p

n, a, b = [int(n) for n in input().split()]
c = 0
m = 0
d = 10**9+7
if n%2==0:
    for i in range(0, n//2):
        c = c + combi(n,i) * 2 
    c += combi(n, n//2)
else:
    for i in range(0, n//2+1):
        c = c + combi(n,i) * 2
m += combi(n, a)
m += combi(n, b)
m += 1
print((c-m)%d)