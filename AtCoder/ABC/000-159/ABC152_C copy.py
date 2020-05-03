N = int(input())
P = [int(n) for n in input().split()]
c = 0
curr = 2*10**5+1
for p in P:
    if p < curr:
        curr = p
        c += 1
print(c)
