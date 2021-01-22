N = int(input())
A = [int(n) for n in input().split()]
ans = 0
num = 0
for i in range(2, 1001):
    c = 0
    for a in A:
        if a%i==0:
            c += 1
    if num <= c:
        num = c
        ans = i
print(ans)
